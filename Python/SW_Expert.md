## 정리해야 할 것들

### print 형식 - f"{}" / "".format()   

### counter - from collections import Counter
Counter.most_common()
.count() -> 특정 변수 뽑아내기

### 2차원 배열 선언
// arr = [0 for i range(10)]  ; 크기 10짜리 0으로 초기화된 배열 선언

// 2차원 배열 입력받기;     arr = [list(map(int, input().split())) for _ in range(100)]
**** 2차원 배열에서 가로 배열(행) 입력 받기: arr_rows = arr
**** 2차원 배열에서 세로 배열(열) 입력 받기: arr_cols = [[arr[i][j] for i in range(100)] for j in range(100)]
    arr_cols = list(map(list, zip(*arr)))   //얘도 바꿔줌

** 2차원 배열에서 한 열의 합: sum_arr.append(sum([j[i] for j in arr]))

```py
# 1209. [S/W 문제해결 기본] 2일차 - Sum

for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    sum_arr = []
    arr_1 = []
    arr_2 = []

    for i in range(100):
        sum_arr.append(sum(arr[i][:]))
        sum_arr.append(sum([j[i] for j in arr]))
        arr_1.append(arr[i][i])
        arr_2.append(arr[i][99-i])
        
    sum_arr.append(sum(arr_1))
    sum_arr.append(sum(arr_2))
    print("#{cnt} {max}".format(cnt = n, max = max(sum_arr)))
```   

```py
# 1209 조금 다른 방식

for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr_rows = arr
    arr_cols = [[arr[i][j] for i in range(100)] for j in range(100)]
    arr_cross1 = [arr[i][i] for i in range(100)]
    arr_cross2 = [arr[i][99-i] for i in range(100)]
    arr_sum = []

    for i in range(100):
        arr_sum.append(sum(arr_rows[i]))
        arr_sum.append(sum(arr_cols[i]))
    arr_sum.append(sum(arr_cross1))
    arr_sum.append(sum(arr_cross2))

    print("#{cnt} {max}".format(cnt = n, max = max(arr_sum)))
```

** join 함수 -> 배열을 연달아서 보여주는 함수
** zip 함수 -> 배열 불러오기 처리 (zip *)

SWEA #1226 미로1 문제 - DFS / BFS 
참고: https://mungto.tistory.com/235 

