### **Big O**
: 빅오는 입력값이 커질 때 알고리즘의 실행 시간(시간 복잡도)과 함께 공간 요구사항(공간 복잡도)이 어떻게 증가하는지를 분류하는데 사용된다.

**Big O의 특징**  
- 점근적 실행시간을 표기할 때 가장 널리 쓰이는 수학적 표기법
  - 점근적 실행시간: 입력값 n이 커질 때, 즉 입력값이 무한대를 형할 때 함수의 실행시간의 추이를 의미
  - 충분히 큰 입력에서는 알고리즘의 효율성에 따라 수행 시간이 ㅋ게 차이가 날 수 있다.


**시간 복잡도**  
: 어떤 알고리즘을 수행하는 데 걸리는 시간
- 빅오로 시간 복잡도를 표현할 때는 최고차항만을 표기하며 계수는 무시한다.

**Big O 표기법의 종류**  
1. **O(1)**: 입력값이 아무리 커도 실행시간은 일정하다  
  ex) 해시 테이블의 조회 및 삽입

2. **O(log n)**: 여기서부터 실행 시간은 입력값에 영향을 받음. 웬만한 n의 크기에 대해서도 매우 견고하다.  
  ex) 이진 검색

3. **O(n), 선형 시간 알고리즘**: 입력값만큼 실행 시간에 영향을 받으며 알고리즘을 수행하는 데 걸리는 시간은 입력값에 비례한다.   
  ex) 정렬되지 않은 리스트에서 최댓값 또는 최솟값을 찾는 경우

4. **O(nlog n)**: 병합 정렬을 비롯한 대부분의 효율 좋은 정렬 알고리즘이 이에 해당함. 

5. **O(n^2)**: 버블 정렬같은 비효율적인 정렬 알고리즘이 이에 해당함

6. **O(2^n)**: 피보나치 수를 재귀로 계산하는 알고리즘이 이에 해당함.

7. **O(n!)**: 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제를 브루트 포스로 풀이할 때 이에 해당함. 가장 느린 알고리즘으로 입력값이 조금만 커져도 웬만한 다항시간 내에는 계산이 어렵다.

**공간 복잡도**  
: 빅오는 시간 복잡도 외에도 공간 복잡도를 표현하는데에도 널리 쓰임. trade-off 관계  

**상한과 최악**
- O : 상한
- Ω : 하한
- θ : 평균

!! 주의해야될 점 !! : 빅오 표기법은 정확하게 쓰기에는 너무 길고 복잡한 함수를 '적당히 정확하게' 표현하는 방법일 뿐, 최악의 경우/평균적인 경우의 시간복잡도와는 아무런 관계가 없는 개념임.

**분할 상환 분석**  
: 시간 또는 메모리를 분석하는 알고리즘의 복잡도를 계산할 때, 알고리즘 전체를 보지 않고 최악의 경우만을 살펴보는 것은 지나치게 비관적이라는 이유로 등장.  
