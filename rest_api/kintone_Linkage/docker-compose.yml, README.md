\# kintone\_Linkage (プロトタイプ)



概要

\- Laravel (backend) + React (frontend) の開発用 Docker 構成

\- PostgreSQL

\- ローカル HTTPS（mkcert）対応

\- フロント: https://kintone-linkage.local:8443

\- API:   https://api.kintone-linkage.local:8443



前提

\- Docker / Docker Compose がインストール済み

\- mkcert を使える（ローカル CA をインストールするので管理者権限が必要）

\- `127.0.0.1 kintone-linkage.local api.kintone-linkage.local` を `/etc/hosts` に追加する



例: /etc/hosts に以下を追加（管理者権限）
127.0.0.1 kintone-linkage.local api.kintone-linkage.local



