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

4. 실습 step 1
   1. 환경 구성
      1. main.py로 실행 시키고 swagger 동작 확인
      2. local , prod 별로 config 파일을 만들어 줍니다.
