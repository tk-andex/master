<?php

namespace App\Services;

use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Http;

class KintoneService
{
    protected $domain;
    protected $appId;
    protected $apiToken;

    public function __construct()
    {
        $this->domain = config('services.kintone.domain');
        $this->appId = config('services.kintone.app_id');
        $this->apiToken = config('services.kintone.api_token');
    }

    public function getRecords()
    {
        $url = "https://{$this->domain}/k/v1/records.json";

        $response = Http::withHeaders([
            'X-Cybozu-API-Token' => $this->apiToken,
            'Content-Type' => 'application/json',
        ])->get($url, [
            'app' => (int) $this->appId,
        ]);

        Log::info('Kintone API status: ' . $response->status());
        Log::info('Kintone API body: ' . $response->body());

        if ($response->successful()) {
            return $response->json();
        }

        return null;
    }
}
