## Deque 와 List 차이(속도)

### 시간 복잡도 비교 테이블
* Deque(A Double-ended Queue)  

![Deque](https://user-images.githubusercontent.com/94775103/214496269-e565878d-073d-4c56-b444-dac7fa1112e1.png)  

* List  

![List](https://user-images.githubusercontent.com/94775103/214496270-58723ef3-4b36-403a-94ce-df4c95ada7ae.png)  


### Deque  
Deque(Double-ended) 는 양 끝에 elements를 추가/삭제 한다는 의미이다.  

![Deque(1)](https://user-images.githubusercontent.com/94775103/214497172-b9680d35-cef0-4dbf-95e3-0db8f1de282f.png)  

내부적으로 **double-linkded list로 구현**되어 있다.  
따라서 **양 끝의 요소 추가/삭제 가 O(1)을 의미**한다.  

* 주요 함수:  
  - append() : deque의 right end에 요소 추가
  - appendleft() :  deque의 lef end에 요소 추가
  - pop() : deque의 right end의 요소 삭제
  - popleft() : deque의 left end의 요소 삭제

### List  
덱과는 다르게 python 의 List 는 fixed size memory blocks(array)로 구현되어 있다.  
다음 그림에서 마지막 원소를 삭제하는 것은 O(1) 이지만, 첫 번째 원소를 삭제하면 이후 모든 원소를 앞으로 이동시키기 때문에 
시간 복잡도는 O(n) 이 된다.  

![List(1)](https://user-images.githubusercontent.com/94775103/214497175-ad986dea-e9d8-40e6-894d-2d6e29f97117.png)  

따라서 삽입/삭제가 뒤가 아닌 앞이나 중간에서 발생할 경우 deque 사용을 우선적으로 고려하는 것이 좋다.

```py
# 이때 꼭 모듈을 가져다 사용한다.
from collections import deque

queue = deque()
```

출처 - [[파이썬] 덱 vs 리스트 속도 차이?](https://wellsw.tistory.com/122)
