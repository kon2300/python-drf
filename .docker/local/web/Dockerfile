# Dockerfile (development)
FROM python:3.12-slim

# 環境変数設定
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=src.settings.local

# 必要なシステムパッケージインストール（例: psycopg2 用）
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ作成
WORKDIR /web

# 依存関係を先にコピーしてキャッシュ利用
COPY requirements.txt /web/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
