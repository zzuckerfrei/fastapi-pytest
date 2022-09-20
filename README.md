
# fastapi-pytest

---
fastapi를 사용한 동기, 비동기 방식 테스트 코드

### Features
* pytest
* pytest-asyncio 
* httpx


```
.
├── app                        
│   ├── __init__.py         
│   ├── main.py              
│   └── tests                   
│       ├── __init__.py
│       ├── test_main.py     # 동기 방식 api 테스트 (TestClient)
│       └── test_async.py    # 비동기 방식 api 테스트 (AsyncClient)
│
└── requirements.txt   
```


### Using the applicaiton
```
pip install -r requirements.txt
```
and
```
pytest
```
or
```
pytest test_async.py
pytest test_async.py
```