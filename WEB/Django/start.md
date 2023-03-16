# Django

## INDEX  
1. Django 시작하기
2. 클라이언트와 서버
3. Django 무작정 따라하기
4. 가상환경
5. 프로젝트와 앱
6. 요청과 응답


### 1. Django 란?  

cf -  @(데코레이터); 함수 안에 함수를 감싸서(가져서) 다른 함수를 꾸며주거나 만들어줄 수 있는 것.

* Framework: 서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것(Frame + Work)
    - 장점; 개발 속도 ↑, 검증 코드, 반복성 낮음, 협업 용애
    - 단점; 선택 폭 ↓, 러닝 커브(학습성 ↓)

### 2. 클라이언트와 서버  

* 클라이언트(client) -- requests/responses -- 서버(server)  

* 클라이언트   
    - 웹 사용자의 인터넷에 연결된 장치
    - 웹 브라우저, 서비스 요청 주체  

* 서버  
    - 클라이언트가 접근 시에 서버에서 데이터를 응답해 웹 브라우저에 표시
    
--------------- 필기 조금 더 추가하자 (강의 뒷 부분) ---------------



### 4. 가상환경  

- venv 세팅 및 활성화  


### 5. 프로젝트와 앱
- django-admin startproject ~
- manage.py startapp articles


### 6. 요청과 응답  

- URL -> VIEW -> TEMPLATE 데이터 흐름
- URLs) 말 그대로 주소값
- View) 요청이 들어오면 HTML Page로 응답을 리턴
- Template) 실제 내용 보여주는 파일, 파일 구조나 레이아웃 정의, 

---

cf) 프로젝트 새로 시작할 경우 해야할 일
- 가상환경 만들기(python -m venv venv)
- git 세팅(git init / touch .gitignore)
- 가상환경에 필요한 패키지(라이브러리 설치)
    - source venv/Scripts/activate  (타 os의 경우 scripts가 아닌 bin 폴더)
    - pip install django==3.2.18
    - pip freeze > requirements.txt
    - 끌어올 때는 pip install -r requirements.txt
- django 의 경우; django-admin startproject (프로젝트몀) (타겟)
- python -m startapp myapp

url 주소 구성 -> view 함수(실제 기능) -> 응답할 자원 template/ return