INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF]*(n+1) for i in range(n+1)]

#자기자신 최단거리 0 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]= 0

#연결 노드 입력
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

#최단거리 입력하기 (점화식) min(A(a,b),A(a,i)+A(i,b))
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=' ')
        else:
            print(graph[a][b],end=' ')

    print()
