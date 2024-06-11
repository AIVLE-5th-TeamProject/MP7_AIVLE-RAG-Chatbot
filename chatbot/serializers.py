from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    question = serializers.CharField(help_text='사용자 메시지')
    session_id = serializers.CharField(help_text='세션 ID', required=False)

# class FileUploadSerializer(serializers.Serializer):
#     file = serializers.FileField(help_text='업로드할 문서 파일')
