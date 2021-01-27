'''
    구조는 복잡하지만 좀더 빠른 다익스트라 알고리즘 구현하기
    힙을 사용하여 우선순위 큐에 저장하며 heappush,heappop을 사용하여 O(N)의 복잡도를 단축 시킨다.
    V:노드 개수 ,E:간선 개수
    O(ElogV)
'''

import heapq
import sys
input = sys.stdin.readline
#무한대 처리
INF = int(1e9)
print(INF)
#노드 개수 간선 개수
n,m = map(int,input().split())
#시작 노드 입력
start = int(input())

#간선 저장 리스트 설정
graph = [[]for i in range(n+1)]
#시작노드 기준 노드별 최단거리 저장
distance = [INF] *(n+1)
#간선입력 node : a,b root_data: c
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
def dijkstar(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(distance[start],start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstar(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
