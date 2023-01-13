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
