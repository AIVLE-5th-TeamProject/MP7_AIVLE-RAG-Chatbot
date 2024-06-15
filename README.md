<p align="center">
  <a href="https://aivle.kt.co.kr/home/main/indexMain">
    <img alt="KT AIVLE Logo" src="https://github.com/or-m-or/AIVLE-5th-MiniProject7_RAG-Chatbot/blob/master/asset/aivle_logo.png?row=true" width="100" style="border-radius: 50%;" />
  </a>
</p>
<h1 align="center">
    에이블스쿨 지원자들을 위한 QA Chatbot 서비스
</h1>

<img alt="Langchain" src="https://img.shields.io/badge/Langchain-1C3C3C.svg?style=for-the-badge&logo=langchain&logoColor=white"/>
<img alt="python" src ="https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=white"/> 
<img alt="Django" src ="https://img.shields.io/badge/Django-092E20.svg?&style=for-the-badge&logo=Django&logoColor=white"/> 
<img alt="OpenAI" src ="https://img.shields.io/badge/OPENAI-412991.svg?&style=for-the-badge&logo=Openai&logoColor=white"/> 
<img alt="Redis" src ="https://img.shields.io/badge/Redis-FF4438.svg?&style=for-the-badge&logo=Redis&logoColor=black"/>
<img alt="HTML" src ="https://img.shields.io/badge/HTML5-E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=white"/> 
<img alt="CSS3" src ="https://img.shields.io/badge/CSS3-1572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=white"/>
<img alt="JavaScript" src ="https://img.shields.io/badge/JavaScript-F7DF1E.svg?&style=for-the-badge&logo=JavaScript&logoColor=black"/>
<img alt="GASP" src ="https://img.shields.io/badge/GASP-88CE02.svg?&style=for-the-badge&logo=GreenSockt&logoColor=black"/>


---

본 프로젝트는 KT 에이블스쿨 5기 미니프로젝트 7차 결과 산출물로, 신규 지원자들을 위한 RAG 기반 챗봇 서비스입니다. 신규 지원자들을 위한 서비스인 만큼, 보다 정확하고 상세한 답변을 제공하는 것에 중점을 두고 개발되었습니다. <br>
  
현재 `master` 브랜치는 미니 프로젝트의 최종 결과물로 제출된 버전(v1.0)에 해당됩니다.<br>
KT 에이블스쿨에서 진행하는 미니 프로젝트 기간은 종료되었지만 <br>
챗봇의 성능(정확도 및 답변속도) 향상 및 코드 품질 개선을 위해 추가 개발이 계속 진행될 예정입니다.  

---


🔥 [ KT AIVLE School 5기 미니프로젝트 7차 ] RAG Chatbot 구축하기 <br>
💻 개발기간 : 2024.06.03 - 2024.06.13

## 0. 목차
  - [1. 프로젝트 주요 기능](#1-main-feature-v10)
  - [2. 필요한 모듈 설치하기](#2-download-and-installation-window)
  - [3. 프로젝트 빌드 방법](#3-getting-started-window)
  - [4. 사용 방법](#4-usage)
  - [5. 버그 및 문제 발생 시 해결 방법](#5-bugs-and-troubleshooting)
  - [6. 버전 변경 사항 기록보기](#6-changelog)
  - [7. 프로젝트 팀원 소개](#7-team)
  - [8. 지원이 필요할 경우](#8-support-and-contact)
  - [9. 라이선스](#9-license)


## 1. Main Feature (v1.0)


## 2. Download and Installation (Window)

1. 먼저 `Conda` 가상환경을 사용하기 위해 사전에 미리 설치합니다.

2. 이어서 `Redis`를 설치한 후 Redis 서버를 실행합니다.

    1. [Redis 공식 Github 페이지](https://github.com/microsoftarchive/redis/releases) 에서 3.0.504 버전의 ZIP파일을 다운로드합니다. (redis-x.y.z.zip)

    2. 이후 다운로드한  ZIP파일을 원하는 폴더에 압축을 풉니다. 예를 들어, C:\redis 폴더를 사용할 수 있습니다.

    3. 압축을 푼 폴더로 이동한 후, redis-server.exe 파일이 있는지 확인합니다.

    4. `Windows 키 + R` 을 누르고 `cmd` 를 입력한 후 `Enter`를 눌러 명령 프롬프트를 엽니다.

    5. 다음과 같이 명령어를 입력하여 Redis 서버를 실행합니다.
        ```
        $ cd C:\redis
        ```
        ```
        $ redis-server.exe
        ```
        Redis 서버가 성공적으로 실행되면 `Ready to accept connections` 메시지가 표시됩니다.
    
    6. Redis 클라이언트로 정상적으로 연결되었는지 테스트를 합니다.
        - 다른 명령프롬프트를 열고, Redis 디렉토리로 이동합니다.
        ```
        $ cd C:\redis
        ```
        - Redis 클라이언트 실행
        ```
        $ redis-cli.exe
        ```
        - Ping 명령어 실행
        ```
        $ ping
        ```
        `Pong` 응답이 표시되면 Redis 서버가 제대로 작동하고 있는 것입니다.

    7. 추후 Redis 서버를 종료하려면 아래 명령어를 사용할 수 있습니다.
        ```
        $ redis-cli shutdown
        ```

## 3. Getting Started (Window)


1. 현재 레포지토리 본인 로컬로 가져오기
    ```bash
    $ git clone https://github.com/AIVLE-5th-TeamProject/MP7_AIVLE-RAG-Chatbot.git
    ```

3. 이후, 다음 명령어로 프로젝트 빌드에 필요한 디렉토리를 생성합니다.
    ```sh
    $ ./setup.sh
    ```

4. 가상환경을 생성한 뒤 활성화 합니다. 가상환경에서 사용하는 python 버전은 3.11.9 으로 세팅합니다. 아래 명령어를 그대로 실행하면 이름이 MP7, 파이썬 버전 3.11.9를 사용하는 conda 가상환경이 생성됩니다.
    ```
    $ conda create --name MP7 python=3.11.9
    ```

5. 가상환경을 실행한 후, 필요한 모듈을 설치합니다.
    ```
    (MP7)...$ pip install -r requirements.txt 
    ```

6. 데이터베이스 마이그레이션 파일을 생성합니다.
    ```
    (MP7)...$ python manage.py makemigrations
    ```

7. 생성된 마이그레이션 파일을 데이터베이스에 적용시킵니다.
    ```
    (MP7)...$ python manage.py migrate
    ```

8. 관리자 페이지 접근용 슈퍼유저 계정을 생성합니다. 다음과 같이 사용할 Username, Eamil, Password 를 본인이 원하는대로 지정합니다.
    ```
    (MP7)...$ python manage.py createsuperuser

    $ Username (leave blank to use 'your-username'): admin
    $ Email address: admin@example.com
    $ Password: 1234
    $ Password (again): 1234
    Superuser created successfully.
    ```


4. 이제 거의 다 끝났습니다. 가상환경이 활성화 되어 있는지 재확인 하고, Redis 서버가 잘 실행 되고 있는지 확인한 뒤, Django 서버를 실행하고 접속합니다. <br>
    (주의) Django 서버가 실행되기 전에 꼭 Redis 서버가 먼저 실행 중이어야 합니다. 
    ```
    $ conda activate mini7   
    $ python manage.py runserver
    ``` 
    서버를 실행하면 database 폴더 하위에 SQlite에서 제공하는 ChromaDB가 생성됩니다.


5. 메인(루트) 페이지에 접근하려면 http://127.0.0.1:8000/ 으로 접속합니다.

10. admin 페이지에 접근 하려면 http://127.0.0.1:8000/admin 으로 접속합니다.

11. swgger 문서를 통해 API 테스트를 해보려면 http://127.0.0.1:8000/swagger 으로 접속합니다.


## 4. Usage





## 5. Bugs and Troubleshooting


## 6. Changelog

## 7. Team

|<img src="https://avatars.githubusercontent.com/u/135506789?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/96802693?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/91467204?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/79041288?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/59814174?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/133032166?v=4" width="150" height="150"/>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|taehwan heo<br/>[@or-m-or](https://github.com/or-m-or)|TaeHui Kim<br/>[@taehui7439](https://github.com/taehui7439)|Yeseo Kim<br/>[@xeonxeonx](https://github.com/xeonxeonx)|[@Han-sangwon](https://github.com/Han-sangwon)|[@Polasia](https://github.com/Polasia)|[@yhjin62](https://github.com/yhjin62)|


## 8. Support and Contact

`mail` : htth815@gmail.com <br>
`kakao Talk ID` : hth815<br> 
`GitHub Issues` : [Open an issue]()<br>
`Feature Requests` : [Feature Requests]()

## 9. License





