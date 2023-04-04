# Prim Algorithm  
: 초안

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
