# 크루스칼 알고리즘 (Kruskal Algorithm) <br>
## 개념  


- 가중치 무방향 그래프 내의 모든 정점을 가장 적은 비용으로 연결하기 위해 사용
- 즉, 최소 신장 트리를 구하기 위한 알고리즘이다. 

![Kruskal](https://i.imgur.com/mCywucG.png)
- 이미지 출처: [출처](https://chanhuiseok.github.io/posts/algo-33/)

> **신장트리** (Spanning Tree): 1) 그래프의 모든 정점을 포함, 2) 정점 간 서로 연결 3) 사이클이 존재하지 않음 (트리)  <br>
> **최소신장트리** (Minimum Spanning Tree, MST): 가중치의 합이 최소가 되는 신장 트리 <br>
 
- 최소 비용이 되려면 그래프가 사이클을 형성하지 않아야 한다 (정점 연결에 불필요한 간선이 있게 됨).
    - 사이클 형성: 한 정점에서 출발해서 선분을 한 번씩 지나서 출발점으로 되돌아올 수 있음
- 간선의 수가 (정점 - 1) 개일 때 최소의 비용을 갖게 된다. 
- 하나의 그래프에서 최소신장트리는 하나 이상 존재할 수 있다. 
- 최소신장트리를 찾는 알고리즘에는 크루스칼 알고리즘과 프림 알고리즘이 있다.
    - 크루스칼(Kruskal): 간선을 기준으로 트리 형성 <br>
    - 프림(Prim): 정점을 기준으로 트리 형성



## 알고리즘 설명 

1. 그래프 간선을 가중치에 따라 오름차순으로 정렬한다. 
2. 간선을 순서대로 선택하되, 사이클이 형성될 경우에는 선택하지 않는다. 
   - 사이클 여부는 Union-Find를 통해 판단한다. 
3. 선택한 간선이 (정점의 개수-1)개가 되면 종료한다. 


## 코드 

```python
#### union find 구현 ################# 
# 특정 원소가 속한 집합을 찾는다 
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
####################################

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

edges = []
# 비용을 담을 변수 result
result = 0

# 간선을 입력받아 cost를 기준으로 오름차순 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

# 가중치가 적은 간선부터 확인 
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않으면 (두 노드의 루트 노드가 서로 다르면)
    if find_parent(parent, a) != find_parent(parent, b):
        # 신장 트리에 간선 추가
        # 두 노드가 연결되었으므로 속한 집합을 합친다. 
        union_parent(parent, a, b)
        result += cost

# 최소 비용 출력
print(result)

```



### 참조 사이트 
- [링크1](https://chanhuiseok.github.io/posts/algo-33/) <br>
- [링크2](https://maetdori.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Minimum-Spanning-Tree-MST-%EC%B5%9C%EC%86%8C-%EC%8B%A0%EC%9E%A5-%ED%8A%B8%EB%A6%AC)
- [링크3](https://deeppago.tistory.com/m/31)