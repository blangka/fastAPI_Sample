> 참고 url : https://fastapi.tiangolo.com/ko/  
> 참고 강의 : https://www.youtube.com/watch?v=ktGVFmfGiGM&list=PLKy1qiqTzJteucwpykHuZyCh-HqeZXIG4&index=18  
> 참고 github : https://github.com/riseryan89/notification-api

1. 환경 세팅

    ```bash
    $ pip install fastapi
    $ pip install uvicorn
    ```

2. 간단한 예제

    ```python
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {"item_id": item_id, "q": q}
    ```

3. 실행

   ```bash
        $ uvicorn main:app --reload
   ```

4. 확인  
   http://127.0.0.1:8000/docs

## 프로젝트 관련 세팅

1. git의 특정 history 받는 방법
   ```bash
     $ git reset --hard d21f2ea194747194b6a54eaeabf8d11f5045c317
   ```  

2. 프로젝트 생성 순서
    1. 파이참 기준으로 생성 합니다. 가상환경을 만듭니다.
   > File -> New -> Project -> Python -> Python Virtual Environment 3.8로 생성한다.  
   > 프로젝트 이름은 noti 로 한다.
   ```bash
        $ virtualenv venv
        $ source venv/bin/activate
   ```   
   > 가상환경을 실행 시킨 다음에 아래와 같이 requirements.txt 파일을 만들어 줍니다.
   ```bash
        $ pip freeze > requirements.txt
   ```
   > run configuration 설정에서 가상환경으로 python interpreter를 설정해 줍니다.   
   > 그러면 절대 경로로 인식하고 프로젝트 수행 가능합니다. (https://velog.io/@shy9664/venv-setting)

3. 프로젝트 기본 설정
    1. [Uvicorn](https://chacha95.github.io/2021-01-16-python6/) : 비동기 역활
    2. [FastAPI](https://fastapi.tiangolo.com/ko/) : API 서버 역활
    3. common : 공통 모듈 , config : 환경변수 관련 모듈(local,prod 나눌수 있음)

4. 실습 step 1 환경구성
    1. main.py로 실행 시키고 swagger 동작 확인
    2. local , prod 별로 config 파일을 만들어 줍니다.
    3. from app.common.config import conf 가 정상적으로 동작하려면 export PYTHONPATH=$PWD 를 실행 시켜준다.  

5. 실습 step2 DB 연결
    1. [sqlalchemy](https://docs.sqlalchemy.org/en/14/) : ORM 을 사용한다.
    2. [mysql 설치 방법 및 dbear setting](https://citronbanana.tistory.com/11) , [mysql password 잃어 버렸을때](https://velog.io/@sorzzzzy/MySQL-Mac-MySQL-root-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%B4%88%EA%B8%B0%ED%99%94%ED%95%98%EA%B8%B0)  
    3. config에 있는 db 정보를 가지고 db를 연결한다. db 연결 code는 database/conn.py 이다.  
    4. 최초에 user 에 대한 테이블을 만들어 준다.
    5. router도 나누어 주어서 / 에서 DB에 직접 insert 추가

6. 실습 step3 회원가입만들기
   1. pydantic을 사용하여 회원가입을 만든다.
   2. main.py에 routes/auth.py를 추가한다. 회원 가입 로그인 기능 추가.
   3. jwt token 을 활용하고 암복호화로 회원 가입 기능 추가
   4. models.py에서 사용되는 모델들의 기능 추가