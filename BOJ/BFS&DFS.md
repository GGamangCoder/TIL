# DFS(깊이 우선 탐색, Depth-First Search)
<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif" height="300px" width="300px"></p>

* **개념**  
: 시작 노드에서 시작해서 다음 분기(branch)로 넘어가기 전에 **해당 분기를 완벽히 탐색 후** 다른 분기로 넘어가는 방식.  
: 여기서 분기는 갈림길이 있던 장소까지 되돌아간다는 것이다.  
: 이 알고리즘을 끝에서부터 부모노드로 돌아가는 것은 백트래킹(backtracking)이라고 한다.  
: 단순 검색 속도 자체는 BFS보다 느리다.

* 장점  
    - 단지 현 경로상의 노드들만을 기억하면 되므로 저장공간의 수요가 비교적 적다.  
    - 목표노드가 깊은 단계에 있을 경우 해를 빨리 구할 수 있다.  
* 단점
    - 해가 없는 경로에 깊이 빠질 가능성이 있다. 따라서 실제의 경우 미리 지정한 임의의 깊이까지만 탐색하고 목표노드를 발견하지 못하면 다음의 경로를 따라 탐색하는 방법이 유용할 수 있다.  
    - 얻어진 해가 최단 경로가 된다는 보장이 없다. 이는 목표에 이르는 경로가 다수인 문제에 대해 깊이우선 탐색은 해에 다다르면 탐색을 끝내버리므로, 이때 얻어진 해는 최적이 아닐 수 있다는 의미이다.   

## 소스 코드
```py
def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = [(x,y)]
    arr[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if arr[nx][ny] == 1:
                    queue.append((nx, ny))
                    arr[nx][ny] = 0
```


# BFS(너비 우선 탐색, Breath-First Search)
<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif" height="300px" width="300px"></p>

* **개념**  
: DFS와는 다르게 깊이가 아닌 넓이를 우선시 하여 탐색한다. 첫 시작 노드에서 연결된 노드를 다음 타겟으로 정하면서 진행된다.

* 장점
    - 출발노드에서 목표노드까지의 최단 길이 경로를 보장한다.
* 단점
    - 경로가 매우 길 경우에는 탐색 가지가 급격히 증가함에 따라 보다 많은 기억 공간을 필요로 하게 된다.
    - 해가 존재하지 않는다면 유한 그래프(finite graph)의 경우에는 모든 그래프를 탐색한 후에 실패로 끝난다.
    - 무한 그래프(infinite graph)의 경우에는 결코 해를 찾지도 못하고, 끝내지도 못한다.

## 소스 코드
```py
def dfs(graph, start_node):
  visit = list()
  stack = list()
  
  stack.append(start_node)
  
  while stack:
    node = stack.pop(0)
    if node not in visit:
      visit.append(node)
      stack.extend(graph[node])
      
  return visit
```
