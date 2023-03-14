### **Generator**
: 루프의 반복 동작을 제어할 수 있는 루틴 형태
- yield: 제너레이터를 리턴할 수 있음. 중간 값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다.

    ```
    def get_natural_number():
      n = 0
      while True:
        n+=1
        yield n
    ```
- 함수의 리턴 값은 **제너레이터**가 된다.
    ```
    get_natural_number()
    <generator object get_natural_number at ~>
    ```
- next: 다음 값을 생성 시 사용
  ```
  g = get_natural_number()
  for _ in range(0, 100):
    print(next(g))
  ```
- 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능능
  ```
  def generator():
    yield 1
    yield 'string'
    yield True
  
  g = generator()
  >>> next(g)
  1
  >>> next(g)
  'string'
  >>> next(g)
  True
  ```

### **range**
: 제너레이터의 방식을 활용하는 대표적인 함수

- range 클래스를 리턴
- for문에서 사용할 경우, 내부적으로는 제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성
- range 클래스를 이용하면 메모리 점유율을 낮출 수 있음 -> 생성 조건만 보관하고 있기 때문
- 인덱스로 접근할 때에도 바로 생성하도록 구현되어 있기 때문에 리스트와 동일한 느낌으로 불편없이 사용할 수 있다.

### **enumerate**
: 여러 가지 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴한다.
- list()로 결과를 추출할 수 있다.
  ```
  a = [1,2,3,2,45,2,5]
  >>> enumerate(a)
  <enumerate object at 0x1010f83f0>
  >>> list(enumerate(a))
  [(0,1), (1,2), (2,3), ...]
  ```
- 리스트와 인덱스의 값을 함께 출력하는 방법
  ```
  for i, v in enumerate(a):
    print(i, v)
  ```

### **locals**
: 로컬 심볼 테이블 딕셔너리를 가져오는 메소드. 로컬 스코프에 정의된 모든 변수를 출력하기 때문에 편리하다.

- 스코프: 파이썬 변수의 유효 범위
- 로컬 변수: 해당 함수의 범위 내에서만 사용 가능
- 글로벌 변수: 광범위한 스코프를 가진 변수로써 선언만 되어있으면 어느 위치에서든 참조할 수 있다.

  - 글로벌 변수의 값을 함수 내에서 수정하고 싶으면 global 키워드를 붙여서 선언하면 됨.
    ex) global 변수명
