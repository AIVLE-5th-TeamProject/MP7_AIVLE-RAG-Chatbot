<p align="center">
  <a href="https://aivle.kt.co.kr/home/main/indexMain">
    <img alt="KT AIVLE Logo" src="https://github.com/or-m-or/AIVLE-5th-MiniProject7_RAG-Chatbot/blob/master/asset/aivle_logo.png?row=true" width="100" style="border-radius: 50%;" />
  </a>
</p>
<h1 align="center">
    에이블스쿨 지원자들을 위한 QA Chatbot 서비스
</h1>

🔥 KT AIVLE School 5기 미니프로젝트 7차 : RAG Chatbot 구축하기 <br>
💻 개발기간 : 2024.06.03 - 2024.06.13

## 소개




## 주요 요구사항 체크리스트

> 구성

- [v] [공통요구사항] RAG를 위해 Vector DB(Chroma sqlite3) 사용할 것
- [] [공통요구사항] 채팅 사용기록 저장, 업로드한 문서를 관리하기 위한 RDB 사용할 것(Sqlite3) 
  - 업로드한 문서관리만 가능한 상태
- [v] [기본요구사항] LLM : gpt-3.5-turbo, Embedded model : text-embedding-ada-002

> 데이터 수집

- [v] [기본요구사항] 홈페이지 FAQ 데이터 수집(질문-답변을 하나의 청크로 사용할 것)
- [] [추가요구사항] 추가 데이터 수집 - 에이블스쿨 홈페이지 다른 게시물
- [] [추가요구사항] 추가 데이터 수집 - 에이블스쿨 팜플릿
- [] [추가요구사항] 추가 데이터 수집 - 네이버 카페

> 서버 기능 구현

- [v] [기본요구사항] 채팅페이지 - 단발성 질문 답변 기능 구현
- [v] [추가요구사항] 채팅페이지 - 대화가 이어지도록 구성(세션 안에서 메모리 관리)
- [v] [+추가요구사항] 채팅페이지 - 채팅 초기화 가능(현재 채팅 기록 초기화)
- [] [추가요구사항] 관리자페이지 - 사용 이력 표 형태로 조회 가능(일자/기간 기준으로 필터링 가능)
- [v] [추가요구사항] 관리자페이지 - 임베딩된 문서 조회 가능(VectorDB 조회)
- [] [추가요구사항] 관리자페이지 - 새로운 문서 업로드 가능(CSV, PDF 등), 유사도 기준으로 업로드 제약조건 지정하기
  - CSV만 가능한 상태

> 클라이언트 기능 구현

- [] [기본요구사항] 웹-모바일 모두 접속 가능
- [v] [기본요구사항] 메인 페이지 UI 구현(간단한 info, 바로가기 화면에 제공)
- [v] [기본요구사항] 채팅 페이지 UI 구현
- [v] [+추가요구사항] 현재 진행 중인 채팅 기록 화면에 표시하기
- [] [+추가요구사항] GPT가 답변할 때 참조한 문서 내용 답변과 함께 출력하기
- [] [+추가요구사항] 본인이 사용했던 채팅 기록 왼쪽 사이드바로 제공

> 웹 서버

- [v] [기본요구사항] 웹 서버에 VectorDB 저장
- [v] [기본요구사항] 간단한 방화벽 설정, ip를 통해 사이트 공개
- [] [추가요구사항] 클라우드 환경 구축


> 성능 개선

- [] [+추가요구사항] 답변 성능 개선 - 프롬프트 엔지니어링 (Few-show 적용 등)
- [] [+추가요구사항] 답변 성능 개선 - Agent, Tools 사용
- [] [추가요구사항] 답변 성능 개선 - 데이터 추가 수집 및 전처리
- [] [+추가요구사항] Message Queue 사용


## 팀원 소개

## 시작 가이드

### 개발 환경 설정

### 개발 빌드

1. 현재 레포지토리 본인 로컬로 가져오기
```
>> git clone https://github.com/AIVLE-5th-TeamProject/MP7_AIVLE-RAG-Chatbot.git
```
이후 해당 프로젝트를 VScode로 열어줍니다.

2. 가상환경 생성 및 활성화하기
```
>> conda create --name MP7 python=3.11.9
>> conda activate MP7
```

3. 가상환경에 필요한 모듈 설치
```
>> pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션 파일 생성
```
>> python manage.py makemigrations
```

5. 생성된 마이그레이션 파일 데이터베이스에 적용
```
>> python manage.py migrate
```

6. 장고 서버 개발모드로 실행
```
>> cd [현재 프로젝트 루트 디렉토리 경로]
>> python manage.py runserver
```

7. 관리자 페이지 접근용 슈퍼유저 생성 이후 아래와 같이 사용할 Username, Email, Password 지정
```
>> python manage.py createsuperuser


>> Username (leave blank to use 'your-username'): admin
>> Email address: admin@example.com
>> Password: aivle202405
>> Password (again): aivle202405
Superuser created successfully.
```

8. 로컬에서 서버 실행 및 접속
```
>> python manage.py runserver

-----vector_store 초기화 완료-----
-----retriever 초기화 완료-----
-----RAG chain 초기화 완료-----
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 12, 2024 - 04:31:12
Django version 5.0.6, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
서버를 실행하면 자동으로 database 폴더 하위에 SQlite에서 제공하는 ChromaDB가 생성됩니다.


9. 웹 페이지에 접근 (로컬에서 실행 중)하려면 http://127.0.0.1:8000/ 으로 접속합니다.

10. admin 페이지에 접근 하려면 http://127.0.0.1:8000/admin 으로 접속합니다.

11. swgger 문서를 통해 API 테스트를 해보려면 http://127.0.0.1:8000/swagger 으로 접속합니다.



배포시 settings.py 의 DEBUG = False 으로 변경합니다.
 settings.py에서 MEDIA_URL = '/media/' 추가

 
## 기술 스택

## 아키텍처


