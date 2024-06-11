"""
뷰 함수 정의 : 사용자 요청 처리, HTTP 응답 반환 
"""
import os
import csv
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin

from langchain.schema import Document

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# from .generation import chat_generation, update_vector_store, initialize_vector_store, initialize_chain
from .serializers import MessageSerializer 
from .models import Documents
from django.apps import apps
import uuid

    
class ChatbotIndexView(TemplateView):
    template_name = "chatbot/index.html"
    
    @swagger_auto_schema(
        operation_id='첫 접속 시 새 채팅 시작',
        operation_description='채팅 페이지 첫 접속 시 새로운 세션 생성',
        tags=['Chat'],
        request_body=MessageSerializer,
        responses={200: 'Success'}
    )
    def get(self, request, *args, **kwargs):
        if not request.session.get('session_id'):
            session_id = str(uuid.uuid4())
            request.session['session_id'] = session_id
            request.session['question'] = None
            request.session['answer'] = None
            print(f'새로운 세션 생성 >> {session_id}')
        
        return render(request, self.template_name)
   

class StartNewSessionView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_id='버튼을 눌러 새로운 채팅 시작하기',
        operation_description='유저가 새로운 채팅 시작 버튼을 누르면 새로운 세션으로 변경(현재 대화 문맥가 다른 별도의 대화 시작)',
        tags=['Chat'],
        request_body=MessageSerializer,
        responses={200: 'Success'}
    )
    def post(self, request):
        # 아직 미완성 API
        # 여기에 기존 세션에 존재하는 채팅 내용 DB에 저장하는 기능 구현 필요
        
        # 기존 세션 삭제
        request.session.flush()
        
        # RAGPipeline 객체 초기화
        apps.get_app_config('chatbot').initialize_pipeline()
        print(f'새로운 RAGpineline 객체 생성')
        
        # 새로운 세션 생성        
        session_id = str(uuid.uuid4())
        request.session['session_id'] = session_id
        request.session['question'] = None
        request.session['answer'] = None
        print(f'새로운 세션 생성 >> {session_id}')
        
        return JsonResponse({'message': 'New session started', 'session_id': session_id})
 

class ChatbotResponseView(APIView, TemplateResponseMixin):
    permission_classes = [AllowAny]
    # parser_classes = [JSONParser]
    template_name = "chatbot/result.html"

    @swagger_auto_schema(
        operation_id='채팅 쿼리 송수신',
        operation_description='사용자로부터 쿼리를 입력받고 LLM으로부터 받은 답변 반환, 브라우저에서 새로 고침 시 현재 채팅 내용 유지',
        tags=['Chat'],
        request_body=MessageSerializer,
        responses={200: 'Success'}
    )
    def post(self, request):
        print("ChatbotResponseView POST 호출됨")
        question = request.data.get('question')
        session_id = request.data.get('session_id')

        # 전역 pipeline 객체 가져오기
        pipeline = apps.get_app_config('chatbot').pipeline
        
        answer = pipeline.chat_generation(question, session_id) 
        request.session['question'] = question
        request.session['answer'] = answer
        # context = {'question': question, 'answer': answer}
     
        # return render(request, 'chatbot/result.html', context)
        # return JsonResponse({'question': question, 'answer': answer}) # API 호출 반환 용
        return JsonResponse({'answer': answer})


    def get(self, request, *args, **kwargs):
        # 브라우저에서 새로고침을 누르면 기존 세션에서 질문과 답변을 가져옴
        session_id = request.session.get('session_id')
        question = request.session.get('question')
        answer = request.session.get('answer')

        # 만약 세션이 없으면, 새로운 세션 생성
        if not session_id:
            session_id = str(uuid.uuid4())
            request.session['session_id'] = session_id
            question = None
            answer = None
            print(f'새로운 세션 생성 >> {session_id}')

        context = {'question': question, 'answer': answer}
        return render(request, 'chatbot/result.html', context)


# request.session.flush() 세션 삭제


'''
아래는 파일 업로드 및 검증 수행하는 API (사용하려면 주석 풀고, urls.py도 주석 풀 것)
=> Admin 페이지에서만 접근 가능하게 수정함.
'''
# @method_decorator(csrf_exempt, name='dispatch') # CSRF 토큰 검증을 비활성화 - 말고 다른 방법은 없는지...
# @method_decorator(staff_member_required, name='dispatch') # 관리자만 접근 가능
# class UpdateDocumentView(APIView):
#     permission_classes = [AllowAny]
#     parser_classes = [MultiPartParser, FormParser]

#     file_param = openapi.Parameter(
#         'file',
#         openapi.IN_FORM,
#         description="업로드할 문서 파일",
#         type=openapi.TYPE_FILE,
#         required=True
#     )

#     @swagger_auto_schema(
#         operation_id='문서 업로드 및 벡터 DB에 추가',
#         operation_description='[Admin Only] 문서를 업로드하고 벡터 DB에 추가합니다.',
#         tags=['Documents'],
#         manual_parameters=[file_param],
#         responses={200: 'Success'}
#     )
#     def post(self, request):
#         if 'file' not in request.FILES:
#             return JsonResponse({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

#         file = request.FILES['file']

#         # 파일 이름 중복 확인
#         if Documents.objects.filter(filename=file.name).exists():
#             print(f"File {file.name} already exists")  # 터미널에 로그 출력
#             return JsonResponse({'status': '이미 존재하는 파일입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        
#         # DB 내부 파일과 유사도 검증에 실패하면 False 반환함.
#         if not pipeline.update_vector_db(file=file):
#             print(f"Similar document found for {file.name}, file not saved")
#             return JsonResponse({'status': '데이터베이스에 이미 유사한 문서가 존재합니다.'}, status=status.HTTP_409_CONFLICT)
        
#         # Document 모델에 저장(RDB 저장)
#         Documents.objects.create(filename=file.name, file=file)

#         print(f"File {file.name} successfully added to the vector store") 
#         return JsonResponse({'status': '성공하였습니다.'}, status=status.HTTP_200_OK)