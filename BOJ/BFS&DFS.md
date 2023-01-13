# BFS
```py
def bfs(graph, start_node):
  visit = list()
  queue = list()
  
  queue.append(start_node)
  
  while queue:
    node = queue.pop(0)
    if node not in visit:
      visit.append(node)
      queue.extend(graph[node])
      
  return visit
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

