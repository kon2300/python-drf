from src.settings.base import *  # noqa: F403
import os

# デバッグ情報を有効化
DEBUG = True

# 全てのホストからのアクセスを許可（開発時のみ）
ALLOWED_HOSTS = ["*"]

# CORS 設定（フロントエンドが別ポートで動くことが多いため）
CORS_ALLOW_ALL_ORIGINS = True

# データベース設定（docker-compose の db サービスを使用）
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME", "devdb"),
        "USER": os.getenv("DATABASE_USERNAME", "devuser"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "devpass"),
        "HOST": os.getenv("DATABASE_HOST", "db"),
        "PORT": os.getenv("DATABASE_PORT", "5432"),
    }
}

# ログはコンテナの標準出力に直接出す
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
