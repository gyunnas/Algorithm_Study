### **인덴트**  
: 공식 가이드인 PEP 8에 따라 공백 4칸을 원칙으로 함.


### **네이밍 컨벤션**
: 각 단어를 밑줄(_)로 구분하여 표기하는 snake case를 따름.

### **타입 힌트**
: 파이썬은 대표적인 동적 타이핑 언어이지만, 타입을 지정할 수 있는 타입 힌트 기능이 있음.
```
def fn(a: int) -> bool:
```
 -> 타입 힌트가 잘못 지정된 코드는 **Incompatible return value type** 오류가 발생하므로 확인 후 코드를 수정함


### **리스트 컴프리헨션**
: 기존 리스트를 기반으로 새로운 리스트를 만들어 내는 구문. 람다 표현식에 map이나 filter를 섞어서 사용하는 것에 비해 가독성이 훨씬 높다

```
list(map(lambda x: x+10, [1,2,3])) 

[ n*2 for n in range(1, 10 + 1) if n % 2 == 1 ]
```

: 리스트 외에도 딕셔너리 등이 가능하도록 추가되었다.
```
a = {}
for key, value in original.items():
  a[key] = value


a = {key: value for key, value in original.items()}

```