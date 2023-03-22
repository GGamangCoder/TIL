## Pypy3 란?

- 유래; python3의 실행 시 시간이 매우 오래 걸린다는 단점으로, **JIT컴파일 방식**을 도입한 것

<br>

#### 컴파일 언어 vs 인터프리터 언어  
- 컴파일 언어: 소스 코드를 기계어로 컴파일 -> 실행파일 만듦 -> 실행(Run time)
- 인터프리터 언어: 코드를 한 줄씩 읽어가며 실행
- 비교하자면, **소스 전체가 아닌 부분을 수정하여 바로 실행 가능한 것이 인터프리터 언어**이다.

* 차이점
1. 실행 단계의 차이  
> 컴파일 언어는 '컴파일러' 단계가 필요하고 인터프리터 언어는 별도의 컴파일러 과정이 필요하지 않다.

2. 생산속도의 차이  
> 컴파일 언어는 '컴파일' 과정이 들어가기 때문에 인터프리터 언어보다 생산속도가 느리다. 인터프리터 언어는 과정이 단순하기 때문에 생산속도가 빠르다.  

3. 실행속도의 차이  
> 실행속도는 컴파일 언어가 더 빠르다. 컴파일을 한 뒤 생성된 파일에 대해 프로그램이 실행되기 때문에 실시간으로 읽고 수행되는 인터프리터 언어에 비해 훨씬 빠르다.

<br>

#### Python 컴파일 과정  
- Cpython 은 가장 처음 만들어진 python 구현체로, '인터프리터' 이면서 '컴파일러'
- .py 코드를 컴파일하여 bytecode로 바꾸고 그 다음 인터프리터(가상 머신)가 실행
- cf) 인터프리터 실행에는 GIL(Global Interpreter Lock)을 사용. bytecode 를 실행할 때에 여러 개가 아닌 **하나의 thread 만 python 객체에 접근하도록 제한**.  

<br>

#### 그렇다면 JIT 컴파일이란 ?
* JIT(Just in Time) 컴파일: 프로그램 실행하기 전 컴파일 하는 대신, 프로그램 실행 시점에 필요한 부분들을 **즉석으로 컴파일하는 방식**, 인터프리터 하면서 **자주 쓰이는 코드를 캐싱**하기 때문에 인터프리터의 느린 실행 속도를 개선할 수 있다.

#### 정리
- Pypy3는 **자주 쓰이는 코드를 캐싱하는 기능**이 있어, '메모리를 조금 더 사용하여 그것들을 저장하므로써 실행속도를 개선'할 수 있다.
- **간단한 코드** 상에는 **Python3** 가 메모리, 속도 측에서 우세
- **복잡한 코드**(반복) 상에서는 **Pypy3**가 우세
