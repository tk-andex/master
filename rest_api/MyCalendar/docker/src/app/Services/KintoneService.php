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
            if (!$appConfig || !is_array($appConfig)) {
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
     * @param string|null $query Kintone query (例: 'user_id = "xxx" limit 1')
     * @param array $fields 取得するフィールドの配列（空: 全フィールド）
     * @return array レスポンスの配列。失敗時は ['records'=>[]] を返す。* 
     */
    public function getRecords(?string $query = null, array $fields = []): array
    {
        $url = "https://{$this->domain}/k/v1/records.json";

        $params = [
            'app' => (string) $this->appId,
        ];
        if ($query !== null) {
            $params['query'] = $query;
        }
        if (!empty($fields)) {
            $params['fields'] = $fields;
        }

        try {
            $response = Http::withHeaders([
                'X-Cybozu-API-Token' => $this->apiToken,
            ])->get($url, $params);

            if ($response->successful()) {
                return $response->json();
            }

            Log::error('Kintone getRecords failed', [
                'status' => $response->status(),
                'body' => $response->body(),
                'params' => $params,
            ]);

            Log::debug('kintone resp sample', $response);

        } catch (\Throwable $e) {
            Log::error('Kintone getRecords exception', [
                'message' => $e->getMessage(),
                'params' => $params,
            ]);
        }

        // 呼び出し側が ['records'] を期待するため、失敗時は空配列構造を返す
        return ['records' => []];
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
}
