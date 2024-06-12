"""
앱의 데이터베이스 테이블 구조를 정의하는 모듈 + API에서 사용할 DAO 정의
"""
from django.db import models

class Documents(models.Model):
    file = models.FileField(upload_to='documents/', default='documents/default.txt')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name