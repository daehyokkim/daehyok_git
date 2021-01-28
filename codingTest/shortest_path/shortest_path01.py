'''
    2021.01.28
    미래도시
    1번부터N번까지의 회사가 서로 도로를 통해 연결되어있다.
    이때 A 1번회사에 있으며 x번 회사에 방문해 물건을 팔려고 한다.
    연결된 두 회사는 양방향으로 이동이 가능하다.
    회사간 이동시간은 1이다.
    A는 K번 회사와 소개팅을 한후 X번 회사에 가사 물건을 팔려고 한다.
    이때 A가 K번화사를 거처 X번 회사로 가는 최소 이동 시간을 출력한다.
    input
        전체  회사 개수 N 경로의 개수 M (1<=N,M<=100) ---> log(N^3)도 허용 --->플로이드 워셸 가능
        둘째줄부터 M+1줄에는 연결된 두 회사의 번호가 공백으로 구분
        M+2번쨰 줄에는 x와 K가 공백으로 구분되어 차례대로 주어진다.
'''
#무한대 사용
import sys
input = sys.stdin.readline
INF = int(1e9)
#노드 수 , 간선 수
print('N M 입력 :')
n,m = map(int,input().split())
#2차원 배열로 생성
graph = [[INF]*(1+n)for i in range(n+1)]

#노드 갯수 입력
print(graph)
print('노드 수만큼 입력 :')
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#x,y
print("x y 입력 : ")
x,k = map(int,input().split())

#자기 자신 최단거리 0초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)
