'''
    DFS와 BFS를 구현해보기
'''


graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
       ]
print(graph)
visited = [False]*9

#DFS구현
#동작원리는 스텍을 사용하고 구현은 재귀함수 기반으로 구현
#dfs(그래프,시작노드,방문확인그래프)
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)

visited = [False]*9
print()
#BFS
#동작원리는 큐를 사용하고 구현 방식은 큐 자료구조로 구현
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

bfs(graph,1,visited)