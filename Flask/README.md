# Python 프로젝트 시작하기


## 목표



Python을 설치하고, 프로젝트를 진행할 수 있는 가상 환경을 만들고, 코드 퀄리티를 일정 수준 이상으로 유지할 수 있도록 테스트와 검사기를 붙인다.
Flask 는 파이썬의 웹서버 프레임워크이다.

## 라이브러리 설치
pip 업그레이드
```bash
pip install --upgrade pip
```

Requierment 파일 활용시 필요 라이브러리를 동시에 설치 가능하다.
```bash
# 라이브러리 설치
pip install -U requests

# 설치된 라이브러리와 버전을 requirements.txt 파일에 기록
pip freeze > requirements.txt

# 의존성 확인
cat requirements.txt

# 설치된 라이브러리 모두 제거
pip freeze | xargs pip uninstall -y

# 라이브러리 설치
pip install -r requirements.txt
```


pytest : 테스트 코드를 작성하고 실행할 수 있도록 pytest를 설치한다. 파일이 수정될 때마다 자동으로 실행하게 하려면 pytest-watch를 쓰면 된다.

```bash
pip install -U pytest
pip install -U pytest-watch
ptw
```

pylama : 올바르게 코딩하는 걸 도울 수 있도록 정적 분석기를 사용하자. 여기서는 Pylava를 이용해 검사한다.



Flask : Java의 Spring과 같은 규칙성을 주어, 효율적으로 코드작업을 할 수 있는 프레임 워크. 대규모 프로젝트시 도움이 된다. 



## 샘플코드 참고



https://palletsprojects.com/p/flask/
sample code를 참고해서 localhost를 띄워 보겠다.
app.py가 기본 인덱스 파일로 잡혀서 로컬을 띄울 수 있다.


샘플코드 작성
```bash
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!' 
    
```

cmd에서 venv를 activate 한 후, 
```bash
$ FLASK_DEBUG=1 flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
FLASK_DEBUG=1를 같이 써주면 수정하면서 바로 새로고침으로 반영된 것을 확인 할 수 있다.(서버 재시작할 필요 없음.)
Hello World가 뜨는 걸 확인 할 수 있다.
