FROM php:8.1-fpm

# 必要な拡張モジュールをインストール
RUN apt-get update && apt-get install -y \
    libpq-dev \
    zip unzip git \
    && docker-php-ext-install pdo pdo_pgsql pgsql

# Composerインストール
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html

# Laravelの依存関係インストールはホスト側で行うか、コンテナ内で実行可能
