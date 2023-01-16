# BFS
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

# DFS
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

