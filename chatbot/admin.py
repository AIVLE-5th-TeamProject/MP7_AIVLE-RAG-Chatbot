"""
Django 관리자 사이트에 모델 등록, 관리하는 모듈
"""

from django.contrib import admin
from django.http import HttpRequest
from .models import Documents
from django.apps import apps
import os


@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')

    def save_model(self, request: HttpRequest, obj: Documents, form, change):
        # 파일 경로 중복 확인
        if Documents.objects.filter(file=f"documents/{os.path.basename(obj.file.path)}").exists(): # aivle_article.csv
            self.message_user(request, "RDB에 같은 파일이 이미 존재합니다.", level='error')
            return

        # 임시로 문서 저장
        super().save_model(request, obj, form, change)
        
        # 전역 pipeline 객체를 가져옴
        pipeline = apps.get_app_config('chatbot').pipeline
        
        # 벡터 DB에 문서 업데이트 시도
        file_path = obj.file.path
        with open(file_path, 'rb') as f:
            if pipeline.update_vector_db(f, obj.file):
                self.message_user(request, "Successfully updated the vector store.")
            else:
                # 유사한 문서가 존재하여 업데이트에 실패 시 저장된 문서 삭제
                obj.delete()
                os.remove(file_path)
                self.message_user(request, "Failed to update the vector store: Similar document found", level='error')
