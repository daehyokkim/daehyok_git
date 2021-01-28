'''
    2021.28
    전보
    N개의 도시가 존재한다. 하지만 x라는 도시에 Y라는 도시로 전보를 보내려면
    X -> Y 가 설치되어져야 한다. EX) x->y 는 존재하나 x <- y 없을 시 y에선 x로 전달 x
    또한 통로를 거쳐 보낼떄 일정 시간이 소요된다.
    이때 지역 C에서 위급상황 메시지를 보낼때 최대한 많이 퍼져나갈 수 있는 도시 수와 모두 메시지를 받는데 걸린
    시간 출력하는 프로그램을 제작하자.
    input
    도시개수 N 통로의 개수 M 메시지를 보내는 도시 C (공뱍으로 분리) : 1<=n<=30,000 1<=M<=200,000 1<=c<=N
    둘째 줄부터 M+1번째 줄 --> 특정도시X --> 특정 도시 Y 잔달되는 시간 Z를 입력 (공백으로 구분) 1<=x,y<=N, 1<=z<=1,000

    output
    도시 C에서 보낸 메시지를 받는 도시의 총 갯수, 총걸린 시간 (공백 구분)
'''
import heapq
import sys
input = sys.stdin.readline
#무한대 설정
INF = int(1e9)
#노드 수 n,간선 m, start c
n,m,c = map(int,input().split())
#간선 담을 그래프
graph = [[]for i in range(n+1)]
#최단거리 설정
distance = [INF]*(n+1)

#간선입력
for _ in range(m):
    x,n,z = map(int,input().split())
    graph[x].append((n,z))

def dijkstar(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstar(c)

#노드 갯수
count = 0
#가장 멀리까지 도달한 시간 합
max_result= 0

for i in distance:
    if i != INF:
        count +=1
        max_result = max(max_result,i)

#출발 노드를 제외해야 하기 때문에 count에 -1을 함
print(distance)
print(count-1,max_result)


