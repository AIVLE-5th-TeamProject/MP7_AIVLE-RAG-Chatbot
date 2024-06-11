"""
core project의 WSGI 구성 : 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점

WSGI callable을 ``application``이라는 변수명을 사용하여 모듈 레벨 변수로 호출함.

참고 : https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
