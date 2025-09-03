<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\KintoneService;

class KintoneController extends Controller
{
    protected $kintoneApp1;
    protected $kintoneApp2;

    public function __construct()
    {
        $this->kintoneApp1 = new KintoneService('app1');
        $this->kintoneApp2 = new KintoneService('app2');
    }

    public function index()
    {
        try {
            $records = $this->kintoneApp2->getRecords();

            if ($records === null) {
                return response()->json(['error' => 'Failed to fetch records'], 500);
            }

            return view('kintone.records', ['records' => $records['records']]);
        } catch (\Exception $e) {
            return response()->json(['error' => $e->getMessage()], 500);
        }
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'employee' => 'required|string',
            'shift_type' => 'required|string',
            'shift_date' => 'required|date',
            'note' => 'nullable|string',
        ]);

        $recordData = [
            'employee' => ['value' => $validated['employee']],
            'shift_type' => ['value' => $validated['shift_type']],
            'shift_date' => ['value' => $validated['shift_date']],
            'note' => ['value' => $validated['note'] ?? ''],
        ];

        $result = $this->kintoneApp2->addRecord($recordData);

        if ($result === null) {
            return response()->json(['error' => 'Failed to add record'], 500);
        }

        return response()->json($result);
    }
}
