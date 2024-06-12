"""
score project의 Django 설정
: 현재 Django 프로젝트의 환경 및 구성을 저장

Django 5.0.6 버전에서 'django-admin startproject'에 의해 생성됨.
참고 : https://docs.djangoproject.com/en/5.0/topics/settings/

전체 설정 목록과 해당 값은 다음을 참고 :
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# load_dotenv()
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# 프로젝트 내에서의 경로를 다음과 같이 빌드 : BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# 빠른 시작 개발 설정 - 프로덕션에는 적합하지 않음
# 참고 : https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: 프로덕션에 사용되는 비밀 키 보안 유지 필요
SECRET_KEY = "django-insecure-iytm&yx-5&2^#uqrm!nkyijav7tdaj0!j)w5mllchsjb#3c5!)"

# SECURITY WARNING: 프로덕션환경에서 DEBUG=True로 실행하지 말 것(개발환경에서만 사용)
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application 초기화
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    'rest_framework',
    'rest_framework.authtoken',
    "chatbot",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# 배포전 이걸로 바꾸기
# API_URL = 'http://18.140.50.229/'
# API_URL = os.getenv('API_URL')
# API_TOKEN = os.getenv('API_TOKEN')


ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')], # template 경로 설정
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# 데이터베이스
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Redis 설정 추가
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://<EC2_INTERNAL_IP>:6379/1", # "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# 비밀번호 유효성 검사
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# # LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = "ko-kr"

# TIME_ZONE = "UTC"
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# 각 앱 아래의 static 폴더를 정적파일 경로로 지정
STATIC_URL = "static/"
MEDIA_URL = '/media/'

# # root 아래의 static 폴더를 정적파일에 추가
STATICFILES_DIRS = [ BASE_DIR / 'static', ]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
