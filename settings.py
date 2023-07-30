import environ
import os

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# デフォルト:SQLite3
# 環境ファイルで指定したデータベースを使用
DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = ['*']