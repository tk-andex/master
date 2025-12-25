FROM php:8.4-fpm

# 必要なシステムパッケージをインストール
RUN apt-get update   && apt-get install -y --no-install-recommends     libpq-dev libzip-dev zlib1g-dev libonig-dev libicu-dev unzip build-essential git curl   && docker-php-ext-configure intl   && docker-php-ext-install -j$(nproc) pdo_pgsql intl mbstring zip   && apt-get clean   && rm -rf /var/lib/apt/lists/*

# composer バイナリをコピー
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

WORKDIR /var/www

# 開発向けの権限設定
RUN chown -R www-data:www-data /var/www

CMD ["php-fpm"]
