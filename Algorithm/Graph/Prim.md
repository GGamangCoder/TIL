# Prim Algorithm  
: 정점 중심의 MST 를 구하기 위한 알고리즘  

<br>

- 알고리즘 구현
```py
import heapq

V, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)]
adj_list = [[] for _ in range(V+1)]

for edge in arr:
    # 시작점 - 가중치, 시작점, 끝점
    adj_list[edge[0]].append((edge[2], edge[0], edge[1]))
    adj_list[edge[1]].append((edge[2], edge[1], edge[0]))


def mst_prim(start_node=0):
    visited = [0] * (V+1)
    res = []
    total = 0

    visited[start_node] = 1
    queue = adj_list[start_node][:]
    heapq.heapify(queue)

    while queue:
        weight, start, end = heapq.heappop(queue)

        if not visited[end]:
            visited[end] = 1
            total += weight
            res.append((start, end, weight))
            for edge in adj_list[end]:
                if not visited[edge[2]]:
                    heapq.heappush(queue, edge)

    return total, res

print(mst_prim())
```

<br>

- SWEA #1251 하나로
```py
maxV = 1000000000000
def Prim():
    # 거리 누적
    distance = [maxV] * N
    distance[0] = 0
    # 방문 여부 체크
    visited = [0] * N
    total = 0
    for _ in range(N):
        min_idx = -1
        min_val = maxV * N
        for i in range(N):
            if not visited[i] and min_val > distance[i]:
                min_idx = i
                min_val = distance[i]
 
        visited[min_idx] = 1
        total += min_val * E
 
        for i in range(N):
            if not visited[i]:
                distance[i] = min(distance[i], (X[min_idx]-X[i])**2 + (Y[min_idx]-Y[i])**2)
 
    return total
 
T = int(input())
for tc in range(1, T+1):
    # 섬의 갯수, N
    N = int(input())
 
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
 
    print('#{} {}'.format(tc, round(Prim())))

```