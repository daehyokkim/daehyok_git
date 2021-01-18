
'''
    노드 0은 노드 1과 간선7으로 연결,노드0은 노드2와 간선5으로 연결
'''
#인접 행렬 구현
#연결이 되지 않은 간선 == 0처리
graph_matrix = [ [0,7,5],
          [7,0,0],
          [5,0,0]]

print(graph_matrix)

#인접 리스트 구현
graph = [[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)