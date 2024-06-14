<p align="center">
  <a href="https://aivle.kt.co.kr/home/main/indexMain">
    <img alt="KT AIVLE Logo" src="https://github.com/or-m-or/AIVLE-5th-MiniProject7_RAG-Chatbot/blob/master/asset/aivle_logo.png?row=true" width="100" style="border-radius: 50%;" />
  </a>
</p>
<h1 align="center">
    에이블스쿨 지원자들을 위한 QA Chatbot 서비스
</h1>

---

본 프로젝트는 KT 에이블스쿨 5기 미니프로젝트 7차 결과 산출물로, 신규 지원자들을 위한 RAG 기반 챗봇 서비스입니다. 신규 지원자들을 위한 서비스인 만큼, 보다 정확하고 상세한 답변을 제공하는 것에 중점을 두고 개발되었습니다. <br>
  
현재 `master` 브랜치는 미니 프로젝트의 최종 결과물로 제출된 버전(v1.0)에 해당됩니다.<br>
KT 에이블스쿨에서 진행하는 미니 프로젝트 기간은 종료되었지만 <br>
챗봇의 성능(정확도 및 답변속도) 향상 및 코드 품질 개선을 위해 추가 개발이 계속 진행될 예정입니다.  

---





🔥 [ KT AIVLE School 5기 미니프로젝트 7차 ] RAG Chatbot 구축하기 <br>
💻 개발기간 : 2024.06.03 - 2024.06.13

## 0. 목차
  - []()


## 1. 구성


## 2. 설치 및 빌드하는 방법

1. 현재 레포지토리 본인 로컬로 가져오기
    ```bash
    >> git clone https://github.com/AIVLE-5th-TeamProject/MP7_AIVLE-RAG-Chatbot.git
    ```

2. 먼저 Redis를 설치한 후 Redis 서버를 실행합니다.

    1. [Redis 공식 Github 페이지](https://github.com/microsoftarchive/redis/releases) 에서 3.0.504 버전의 ZIP파일을 다운로드합니다. (redis-x.y.z.zip)

    2. 이후 다운로드한  ZIP파일을 원하는 폴더에 압축을 풉니다. 예를 들어, C:\redis 폴더를 사용할 수 있습니다.

    3. 압축을 푼 폴더로 이동한 후, redis-server.exe 파일이 있는지 확인합니다.

    4. `Windows 키 + R` 을 누르고 `cmd` 를 입력한 후 `Enter`를 눌러 명령 프롬프트를 엽니다.

    5. 다음과 같이 명령어를 입력하여 Redis 서버를 실행합니다.
        ```
        >> cd C:\redis
        ```
        ```
        >> redis-server.exe
        ```
        Redis 서버가 성공적으로 실행되면 `Ready to accept connections` 메시지가 표시됩니다.
    
    6. Redis 클라이언트로 정상적으로 연결되었는지 테스트를 합니다.
        - 다른 명령프롬프트를 열고, Redis 디렉토리로 이동합니다.
        ```
        >> cd C:\redis
        ```
        - Redis 클라이언트 실행
        ```
        >> redis-cli.exe
        ```
        - Ping 명령어 실행
        ```
        >> ping
        ```
        `Pong` 응답이 표시되면 Redis 서버가 제대로 작동하고 있는 것입니다.


3. 이후, 다음 명령어로 초기 설정을 자동으로 수행할 수 있습니다.
    ```sh
    >> ./setup.sh
    ```
    이 스크립트를 실행하면, `database` 및 `documents` 폴더를 생성하고, conda 가상환경을 설정한 후 필요한 모듈을 설치합니다. 또한, 데이터베이스 마이그레이션을 수행하고 관리자 계정을 생성합니다.

    스크립트 실행 이후, 쉘에 `슈퍼유저 계정을 생성하려면 아래의 프롬프트에 따라 Username, Email, Password를 입력하세요:` 가 출력되면 관리자 페이지에 접근할 때 사용할 `Username`, `Email`, `Password`를 기입합니다.


4. 이제 거의 다 끝났습니다. 가상환경을 활성화 한 뒤, Django 서버를 실행하고 접속합니다. <br>
    (주의) Django 서버가 실행되기 전에 꼭 Redis 서버가 먼저 실행 중이어야 합니다. 
    ```
    >> conda activate mini7   
    >> python manage.py runserver
    ``` 
    서버를 실행하면 database 폴더 하위에 SQlite에서 제공하는 ChromaDB가 생성됩니다.


5. 메인(루트) 페이지에 접근하려면 http://127.0.0.1:8000/ 으로 접속합니다.

10. admin 페이지에 접근 하려면 http://127.0.0.1:8000/admin 으로 접속합니다.

11. swgger 문서를 통해 API 테스트를 해보려면 http://127.0.0.1:8000/swagger 으로 접속합니다.



## 3. 구현된 주요 기능(v1.0)


## 4. 버그 및 문제 해결 방법


## 5. 버전 변경 사항

## 6. 팀 소개

|<img src="https://avatars.githubusercontent.com/u/135506789?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/96802693?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/91467204?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/79041288?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/59814174?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/133032166?v=4" width="150" height="150"/>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|taehwan heo<br/>[@or-m-or](https://github.com/or-m-or)|TaeHui Kim<br/>[@taehui7439](https://github.com/taehui7439)|Yeseo Kim<br/>[@xeonxeonx](https://github.com/xeonxeonx)|[@Han-sangwon](https://github.com/Han-sangwon)|[@Polasia](https://github.com/Polasia)|[@yhjin62](https://github.com/yhjin62)|



## 7. 지원


## 8. 라이선스





