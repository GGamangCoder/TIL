# 다익스트라 알고리즘 (Dijkstra Algorithm)

### 개념

- 최단 경로 알고리즘
- 항상 노드 주변의 최단 경로만을 택하는 그리디 알고리즘, 노드 주변 탐색 시 BFS 이용 

> **최단 경로 알고리즘**  
다익스트라(Dijkstra): 간선의 가중치가 각각 다를 때  
벨만-포드(Bellman-Ford): 음수 가중치의 간선이 있을 때  
플로이드-와샬(Floyd-Warshall): 모든 정점에서 다른 모든 정점 간 최단경로를 구할 때  

### 알고리즘 원리 
1. 출발 노드를 설정한다.    
2. 최단 거리 테이블을 초기화한다 (다른 모든 노드로 가는 최단 거리를 무한으로 초기화)  
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택한다.  
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.   
5. 3-4번 반복 
- 참고: [링크](https://doing7.tistory.com/76)

### 특징 
- 임의의 정점을 출발 집합에 더할 때, 그 정점까지의 최단거리는 계산이 끝났다고 가정하므로 음수 가중치가 있다면 해당 알고리즘을 사용할 수 없다. 음수 가중치가 있다면 최단 경로를 찾지 못할 수 있고, 무한 사이클을 돌 수 있다. 같은 이유로 최장 거리를 구할 때는 다익스트라 알고리즘을 사용할 수 없다. 

### 구현 
2가지 방법
1. 최초 구현 방법 
- 시간 복잡도: O(V^2)
    - V는 노드의 개수, E는 간선의 개수 

```py 
INF = int(1e9) 

# 노드의 개수 n, 간선의 개수 m
n, m = map(int, input().split())
# 시작 노드 start 
start = int(input())
# 노드의 방문 여부를 체크하기 위한 배열
visited = [False]*(n+1)
# 최단 경로 테이블 (무한으로 초기화)
distance = [INF]*(n+1)

# 각 노드의 연결 노드 및 비용 저장 
graph = [[] for i in range(n+1)]

for _ in range(m):
  # 노드 a -> 노드 b, 비용 c 
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중 최단경로가 가장 짧은 노드를 리턴 
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드의 최단 경로는 0, 방문했음을 체크 
    distance[start] = 0
    visited[start] = True
    # 시작 노드와 연결된 노드까지 이동 비용 업데이트 
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 모든 노드에 대해 반복 (시작 노드 제외 n-1개)
    for i in range(n-1):
    # 현재 최단거리가 가장 짧은 노드 가져와 방문 처리 
    now = get_smallest_node()
    visited[now] = True
    # 현재노드까지의 최단거리 + 현재 노드 -> 연결된 노드(j)까지의 거리 계산 
    for j in graph[now]:
        cost = distance[now] + j[1]
      # 지금 계산한 cost가 테이블의 비용보다 짧을 경우 최단경로 테이블 갱신 
        if cost<distance[j[0]]:
            distance[j[0]] = cost 
  
#다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
```


2. 우선순위 큐 사용 방법   
- (시간 복잡도: O(V+E)logV, 모든 정점이 출발지에서 도달 가능하면 O(ElogV)) 
- 파이썬 heapq 라이브러리 사용 

```py
import heapq
import sys

input = sys.stdin.readline 
INF = int(1e9) 

n, m = map(int, input().split())
start = int(input())
# 최단거리 테이블
distance = [INF]*(n+1)

# 노드 연결정보
graph = [[] for i in range(n+1)]

for _ in range(m):
    # 노드 a -> 노드 b, 비용 c
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 다익스트라 알고리즘(최소힙 이용))
def dijkstra(start):
    q=[]
    # 시작 노드
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드였다면 무시
        # 별도의 visited 테이블이 필요없이, 최단거리테이블을 이용해 방문여부 확인
        if distance[now] < dist:
            continue
        # 선택된 노드와 인접한 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
        # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost,i[0]))
  
# 다익스트라 알고리즘수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우
  if distance[i] == INF:
    print("infinity")
  else:
    print(distance[i])
```