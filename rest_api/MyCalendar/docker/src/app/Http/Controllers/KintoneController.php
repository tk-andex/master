<?php

namespace App\Http\Controllers;

use App\Services\KintoneService;

class KintoneController extends Controller
{
    protected $kintone;

    public function __construct(KintoneService $kintone)
    {
        $this->kintone = $kintone;
    }

    public function index()
    {
        try {
            $records = $this->kintone->getRecords();

            if ($records === null) {
                return response()->json(['error' => 'Failed to fetch records'], 500);
            }

            return response()->json($records);
        } catch (\Exception $e) {
            return response()->json(['error' => $e->getMessage()], 500);
        }
    }
}
