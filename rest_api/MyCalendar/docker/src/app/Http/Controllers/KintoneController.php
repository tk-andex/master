<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\KintoneService;
use Illuminate\Support\Facades\Log;
use Illuminate\Pagination\LengthAwarePaginator;
use App\Models\KintoneUser;

class KintoneController extends Controller
{
    protected $kintoneApp1;
    protected $kintoneApp2;

    public function __construct(KintoneService $kintoneApp1, KintoneService $kintoneApp2)
    {
        $this->kintoneApp1 = $kintoneApp1; // 実際には app 名を渡す方法をサービスプロバイダで管理
        $this->kintoneApp2 = $kintoneApp2;
    }

    protected function resolveEmployeeName(string $userId): ?string
    {
        $userId = trim((string) $userId);
        if ($userId === '') {
            return null;
        }

        // 1) DBを優先
        $employee = KintoneUser::where('user_id', $userId)->value('employee');
        $employee = is_string($employee) ? trim($employee) : $employee;

        if (!empty($employee)) {
            return $employee;
        }

        // 2) DBに空があれば kintone から取得（呼び出しは最小限に）
        try {
            // KintoneService::getRecords の仕様に合わせてクエリを作る
            // ここでは user_id フィールドで検索する例
            $query = sprintf('user_id = "%s" limit 1', addslashes($userId));
            $resp = $this->kintoneApp1->getRecords($query, ['employee']); // 取得フィールドを絞る（任意）
            $records = $resp['records'] ?? [];

            if (count($records) > 0) {
                // kintone のフィールド名が 'employee' か 'ユーザー名' など実際のコードに合わせてください
                $kname = $records[0]['employee']['value'] ?? $records[0]['ユーザー名']['value'] ?? null;
                $kname = is_string($kname) ? trim($kname) : $kname;

                if (!empty($kname)) {
                    // 3) DB に保存して次回は DB を使えるようにする
                    KintoneUser::updateOrCreate(
                        ['user_id' => $userId],
                        ['employee' => $kname]
                    );
                    return $kname;
                }
            }
        } catch (\Throwable $e) {
            Log::error('Failed to fetch employee from kintone in resolveEmployeeName', [
                'userId' => $userId,
                'error' => $e->getMessage(),
            ]);
        }

        // どちらも取れない場合は null を返す
        return null;
    }

    public function index(Request $request)
    {
        try {
            $recordsResp = $this->kintoneApp2->getRecords();

            if ($recordsResp === null) {
                return response()->json(['error' => 'Failed to fetch records'], 500);
            }

            $records = $recordsResp['records'] ?? [];

            // user_id の一覧を収集（trimして重複削除）
            $userIds = [];
            foreach ($records as $r) {
                $id = $r['user_id']['value'] ?? null;
                if ($id !== null) {
                    $id = trim((string) $id);
                    if ($id !== '') {
                        $userIds[] = $id;
                    }
                }
            }
            $userIds = array_values(array_unique($userIds));

            // DBからまとめて取得して連想配列にする（キーを文字列で統一）
            $map = [];
            if (!empty($userIds)) {
                $map = KintoneUser::whereIn('user_id', $userIds)
                    ->get(['user_id', 'employee'])
                    ->mapWithKeys(function ($item) {
                        return [trim((string) $item->user_id) => $item->employee];
                    })->toArray();
            }

            // レコードを置換（employee フィールドを確実にセット）
            // DB優先：1) DBのmap 2) kintoneのemployee_key 3) user_id（フォールバック）
            foreach ($records as &$record) {
                // まず user_id 候補を取得（employee_ID や user_id 等）
                $userId = isset($record['employee_ID']['value']) && trim((string) $record['employee_ID']['value']) !== ''
                    ? trim((string) $record['employee_ID']['value'])
                    : (isset($record['user_id']['value']) ? trim((string) $record['user_id']['value']) : null);

                $display = null;

                // 1) DBを優先（$map は user_id => employee）
                if ($userId) {
                    $employeeFromDb = $map[$userId] ?? null;
                    if (!empty(trim((string) $employeeFromDb))) {
                        $display = trim((string) $employeeFromDb);
                    }
                }

                // 2) DBに無ければ kintone の employee_key（表示名）を使う
                if ($display === null) {
                    $employeeKey = $record['employee_key']['value'] ?? null;
                    $employeeKey = is_string($employeeKey) ? trim($employeeKey) : null;
                    if (!empty($employeeKey)) {
                        $display = $employeeKey;
                    }
                }

                // 3) それでも無ければ userId をフォールバック表示
                if ($display === null && $userId) {
                    $display = $userId;
                }

                // 最終的に employee にセット（ビューは employee を優先表示）
                $record['employee'] = ['value' => $display ?? ''];

                // 既存の user_id 表示を上書きしたければ次を有効に（任意）
                if (isset($record['user_id'])) {
                    $record['user_id']['value'] = $record['employee']['value'];
                }
            }
            unset($record);

            // ページネーション（配列からPaginatorを作る）
            $page = $request->get('page', 1);
            $perPage = 10;
            $collection = collect($records);
            $items = $collection->slice(($page - 1) * $perPage, $perPage)->values();
            $paginator = new LengthAwarePaginator(
                $items,
                $collection->count(),
                $perPage,
                $page,
                ['path' => $request->url(), 'query' => $request->query()]
            );

            // API からの呼び出しかどうかで返し分け（API -> JSON、通常 -> view）
            if ($request->wantsJson() || strpos($request->header('Accept', ''), 'application/json') !== false) {
                return response()->json(['records' => $paginator]);
            }

            $employees = KintoneUser::select('user_id', 'employee')->orderBy('id')->get();
            return view('kintone.records', ['records' => $paginator, 'employees' => $employees]);

        } catch (\Exception $e) {
            Log::error('Kintone index error', ['message' => $e->getMessage(), 'trace' => $e->getTraceAsString()]);
            return response()->json(['error' => 'Internal Server Error'], 500);
        }
    }
    public function store(Request $request)
    {
        $validated = $request->validate([
            'user_id' => 'required|string',
            'shift_type' => 'required|string',
            'shift_date' => 'required|date_format:Y-m-d',
            'note' => 'nullable|string',
        ]);

        // DBから従業員名を取得（優先）
        $employeeName = KintoneUser::where('user_id', $validated['user_id'])->value('employee');
        $employeeName = is_string($employeeName) ? trim($employeeName) : null;

        // DBにない場合は kintone から取得してDBに入れる（既存のヘルパー）
        if (empty($employeeName)) {
            $employeeName = $this->resolveEmployeeName($validated['user_id']);
        }

        if (!$employeeName) {
            return response()->json(['error' => 'Employee not found'], 404);
        }

        // 正規化
        $employeeName = trim((string) $employeeName);

        // kintone に送る payload（キー項目 employee_key を使う）
        $recordData = [
            // ここを employee_key にする（カレンダーアプリの「キー項目」フィールドコードを使う）
            'employee_key' => ['value' => $employeeName],
            'shift_type' => ['value' => $validated['shift_type']],
            'shift_date' => ['value' => $validated['shift_date']],
            'note' => ['value' => $validated['note'] ?? ''],
        ];

        Log::info('Sending record to kintone (employee_key)', ['record' => $recordData, 'user_id' => $validated['user_id']]);

        try {
            $result = $this->kintoneApp2->addRecord($recordData);
        } catch (\Throwable $e) {
            Log::error('kintone addRecord threw exception', ['error' => $e->getMessage(), 'payload' => $recordData]);
            return response()->json(['error' => 'Failed to add record to kintone', 'detail' => $e->getMessage()], 500);
        }

        if ($result === null) {
            Log::error('kintone addRecord returned null', ['payload' => $recordData]);
            return response()->json(['error' => 'Failed to add record'], 500);
        }

        return response()->json($result, 201);
    }
    public function create()
    {
        $employees = \App\Models\KintoneUser::select('user_id', 'employee')->orderBy('id')->get();
        return view('kintone.records', compact('employees'));
    }
}
