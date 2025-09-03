<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class KintoneService
{
    protected $domain;
    protected $appId;
    protected $apiToken;

    /**
     * @param string|null $appKey 使用するkintoneアプリのキー（例: 'app1', 'app2'）
     */
    public function __construct(string $appKey = 'app2')
    {
        $this->domain = config('services.kintone.domain');

        if ($appKey) {
            $appConfig = config("services.kintone.apps.{$appKey}");
            if (!$appConfig) {
                throw new \InvalidArgumentException("Kintone app config for '{$appKey}' not found.");
            }
            $this->appId = $appConfig['app_id'];
            $this->apiToken = $appConfig['api_token'];
        } else {
            // デフォルト設定（単一アプリの場合など）
            $this->appId = config('services.kintone.app_id');
            $this->apiToken = config('services.kintone.api_token');
        }
    }

    /**
     * 最新レコード取得
     */
    public function getRecords()
    {
        $url = "https://{$this->domain}/k/v1/records.json";

        $response = Http::withHeaders([
            'X-Cybozu-API-Token' => $this->apiToken,
        ])->get($url, [
                    'app' => (int) $this->appId,
                ]);

        if ($response->successful()) {
            return $response->json();
        }

        Log::error('Kintone getRecords failed', [
            'status' => $response->status(),
            'body' => $response->body(),
        ]);

        return null;
    }

    /**
     * レコード追加
     *
     * @param array $data kintoneのレコード形式でデータを渡す
     * @return array|null
     */
    public function addRecord(array $data)
    {
        $url = "https://{$this->domain}/k/v1/record.json";

        $payload = [
            'app' => (int) $this->appId,
            'record' => $data,
        ];

        $response = Http::withHeaders([
            'X-Cybozu-API-Token' => $this->apiToken,
            'Content-Type' => 'application/json',
        ])->post($url, $payload);

        if ($response->successful()) {
            return $response->json();
        }

        Log::error('Kintone addRecord failed', [
            'status' => $response->status(),
            'body' => $response->body(),
        ]);

        return null;
    }

    /**
     * app2のkintoneからemployeeの値を取得する例メソッド
     * @param string $employeeKey 検索キー（例: 社員コードなど）
     * @return string|null
     */
    public function getEmployeeValueFromApp1(string $employeeKey)
    {
        // app1(ユーザー)用のインスタンスを作成（app1の設定を使う）
        $app1 = new self('app1');

        $url = "https://{$app1->domain}/k/v1/records.json";

        $response = Http::withHeaders([
            'X-Cybozu-API-Token' => $app1->apiToken,
        ])->get($url, [
                    'app' => (int) $app1->appId,
                    'query' => "employee_code = \"{$employeeKey}\" limit 1", // employee_codeはapp2の検索フィールド例
                ]);

        if ($response->successful()) {
            $records = $response->json()['records'] ?? [];
            if (count($records) > 0) {
                return $records[0]['employee_name']['value'] ?? null; // employee_nameは取得したいフィールド名例
            }
        }

        Log::error('Failed to fetch employee from app2', [
            'employeeKey' => $employeeKey,
            'status' => $response->status(),
            'body' => $response->body(),
        ]);

        return null;
    }
}
