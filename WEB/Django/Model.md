# Django: 서버 구현 웹 프레임워크  
> Framework: 코드의 재사용, 서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것  

### 클라이언트와 서버 구조
* 클라이언트(user)
    - 사용자의 인터넷에 연결된 장치(pc 혹은 모바일 등)
    - 웹 브라우저
    - 서비스 요청(request)하는 주체
* 서버(server)
    - 페이지, 사이트 또는 앱을 저장하는 컴퓨터
    - 클라이언트가 접근할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시
    - 요청에 응답하는 주체

### 시작하기  
0. 가상환경 사용 - 모든 프로젝트는 가상환경(venv)을 만들어준 후 실행한다.
    1. 생성 - python -m venv venv
    2. 활성화 - source venv/Scripts/activate
    3. 비활성화 - deactivate
    - 가상환경 패키지 목록 저장; pip freeze > requirements.txt
    - 파일로 부터 패키지 설치; pip install -r requirements.txt
1. Django 설치하기 - pip install django==3.2.18
2. 프로젝트 생성 - django-admin startproject (프로젝트명)
3. 서버 실행 - python manage.py runserver


---

* 구분자

---

### HTML <input> element  

- type 속성에 따라 동작 방식이 달라짐, 별도 MDN 문서 참고
- 기본값은 'text'  

- 핵심 속성; name - 서버가 메시지/데이터 를 받는
- form 을 통해 데이터 제출(submit)했을 때 name 속성 설정 값을 서버로 전송하고, 서버는 그 값을 통해 사용자가 입력한 데이터에 접근할 수 있음
- name 은 key, value 는 value 로 매핑

### HTTP  
- HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환 기초, **리소스가 수행하길 원하는 작업**인 request methods 를 정의  

- HTTP Methods 예시) GET, POST, PUT(수정), DELETE - CRUD
                      |    | -> form 에서

* Get  
-> 서버로부터 리소스 요청 시, 데이터 가져올 때만 사용해야 함
-> 데이터를 서버로 전송할 때 Query String Parameters 통해 전송
-> 데이터는 URL 에 포함되어 서버로 보내짐


---

### Database
- 체계화된 데이터 모임
- 조직화된 데이터 수집하는 저장 시스템

<br>

- 스키마(Scema)
- 테이블(Table)
- PK(Primary Key)

### Model
