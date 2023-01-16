# 수정 반드시 필요

# Binaray Search
어떠한 값을 찾고 싶은데 그 값을 가지고 있는 배열의 수가 많으면 어떻게 될까? <br>
제일 먼저 시도하는 방법은 선형(Linear) 알고리즘일것이다. <br>
10개의 배열이 있다면 제일 처음 0부터 9까지 차례대로 탐색하는 방법이다. 제일 쉬운 방법이지만 제일 멍청한 방법이기도 하다. <br>
선형 알고리즘은 배열의 수가 n개에서 2n 개로 늘어났을때 complexity가 선형적으로 증가하므로 O(N)이다. <br>
일반적인 상황에서는 잘 작동하겠지만 시간단축을 위해서라도 좀 더 좋은 방법이 필요할 것이다. <br>
<br>
이때, 사용해 볼수 있는 것이 이진탐색(Binaray Search)이다. 문자 그대로 이진 탐색 즉, 반씩 나누어 가면서 탐색하는 알고리즘이다 <br>
단, 이진탐색을 사용하기 전 반드시 지켜야할 사항이 있다. 바로, 배열의 정렬이다. <br>
왜 반드시 배열의 정렬이 선행되어야 하는지는 이진탐색의 원리를 이해하면 자연스럽게 이해가 된다.<br>

## Binary Search Algorithm
이진 탐색은 선형 탐색과 다르게 배열의 처음부터 탐색하지 않는다. <br>
대신, 배열의 정중앙에서 시작한다. 이진 탐색은 다음과 같은 4단계로 이루어진다.<br>

1. 정중앙의 값이 우리가 찾고 있는 값이라면 바로 값을 반환할 것이다.
2. 만약 우리가 찾고 있는 값보다 배열의 값이 크다면 우리는 왼쪽배열을 탐색할것이다.
3. 만약 우리가 찾고 있는 값보다 배열의 값이 작다면 우리는 오른쪽배열을 탐색할것이다.
4. 현재 위치와 왼쪽 또는 오른쪽 끝 위치의 중간에서 부터 다시 탐색을 시작한다.

위에 2, 3 번이 이진 탐색의 핵심이다. 위에서 이진탐색을 사용하기 위해선 반드시 배열의 정렬이 필수라고 했던 이유를 알겠는가? <br>
만약 정렬되어 있지 않으면 우리는 필요없는 배열의 반을 또 찾아야 할 것이기 떄문이다.<br>

<p align="center"><img src="https://www.computerhope.com/jargon/b/binary-search.jpg" height="300px" width="300px">
</p>

## Benefit of Binary Search 
그렇다면 왜 이진 탐색이 선형 탐색보다 좋을까? 
바로, 한번의 탐색이 끝날때 마다 배열이 반씩 줄어들기 때문이다. <br>
예를 들면, 배열의 크기가 10에서 20으로 증가한다면 선형 탐색의 경우 연산량도 10에서 20으로 증가하지만 이진 탐색은 3에서 4로만 증가한다.<br>
배열은 2배가 되었는데 검색 스텝은 단 1만 증가하였다. <br>
이것을 Big O로 나타내면 O(log N) 이다.<br>
선형 탐색에 비해 압도적인 차이가 난다는 것을 확인할 수 있다.

## Code
비재귀적 Python
```python
def binary_search (arr, val):
    first, last = 0, arr.len()
    while first<=last:
        mid = (first + last) // 2
        if arr[mid] == val: return mid
        if arr[mid] > val: last = mid - 1
        else: first = mid+1
    return -1
```
재귀적 Python
```python
def binary_search_recursion (target, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        
    return binary_search_recursion(target, start, end, data)
```
반복 C++
```cpp
// 이진 탐색 소스코드 구현(반복문)
int binarySearch(vector<int>& arr, int target, int start, int end) {
    while (start <= end) {
        int mid = (start + end) / 2;
        // 찾은 경우 중간점 인덱스 반환
        if (arr[mid] == target) return mid;
        // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        else if (arr[mid] > target) end = mid - 1;
        // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else start = mid + 1; 
    }
    return -1;
}
```

재귀적 C++
```cpp
// 이진 탐색 소스코드 구현(재귀 함수)
int binarySearch(vector<int>& arr, int target, int start, int end) {
    if (start > end) return -1;
    int mid = (start + end) / 2;
    // 찾은 경우 중간점 인덱스 반환
    if (arr[mid] == target) return mid;
    // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else if (arr[mid] > target) return binarySearch(arr, target, start, mid - 1);
    // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else return binarySearch(arr, target, mid + 1, end);
}
```

### 참고
* https://github.com/ndb796/python-for-coding-test
