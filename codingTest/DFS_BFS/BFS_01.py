'''
    2021.01.15
    미로탈출
    N * M 크기의 직사각형 미로에서 출발위치(1,1)에서 출구(N,M)의 위치에 존재하ㄴ며 한번에 한칸씩 이동가능.
    괴물의 위치 = 0, 괴물 x = 1 일때
     출발지에서 출구까지 최소칸의 개수를 구하시오. 단.칸의 갯수는 시작킨과 마지막칸 모두 포함해서 계산.
     input
     n m ## 4<=N , =m<= 200
     N*M미로 입력 ##마지막 칸은 항상 1이다.

     output
     최소 이동 칸의 갯수

     문제를 풀기 위한 사용 알고리즘
      DFS/BFS 중 가장 근접한 위치를 차근차근 테스트 하며 최종 결과를 얻을 수 있는 BFS가 문제에 가장 적합하다.

'''

from collections import deque

##BFS 설정
def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]

            #범위에 벋어난 좌표 처리
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #괴물 존재시 처리
            if graph[nx][ny]==0:
                continue
            #이동좌표 표시
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx,ny))

    return graph[n-1][m-1]

#n,m
n,m = map(int,input().split())
graph=[]
dx=[-1,1,0,0]#상하우좌
dy=[0,0,1,-1]#상하우좌

for i in range(n):
    graph.append(list(map(int,input())))
print(graph)
print(bfs(0,0))