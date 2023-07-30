import environ
import os
import dj_database_url

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

default_dburl = "postgresql://user_name:password@localhost:port/database_name"
DATABASES = {'default': dj_database_url.config(default=default_dburl)}

# デフォルト:SQLite3
# 環境ファイルで指定したデータベースを使用
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2', # PostgreSQL使いますよ宣言
        'NAME': 'chat_japanese', # データベース名
        'USER': 'chat_user', # データベースに接続するDBユーザー名
        'PASSWORD': 'password1', # データベースに接続する際のDBユーザのパスワード
        'HOST': '', # 'localhost'
        'PORT': '', # 5432
    }
}

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

dotenv.load_dotenv() # .env ファイルを読み込む
SECRET_KEY = os.getenv('SECREST_KEY') # .env内の環境変数を取得
SUPERUSER_NAME = os.getenv('SUPERUSER_NAME')
SUPERUSER_EMAIL = os.getenv('SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = os.getenv('SUPERUSER_PASSWORD')

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# 以下を追加
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
