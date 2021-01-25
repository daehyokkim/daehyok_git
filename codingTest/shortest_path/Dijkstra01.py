'''
    2021.01.25
    간단한 다익스트라 알고리즘(구현은 쉽지마 느리게 동작하는 코드)
    V:노드 개수
    시간복잡도
        O(V^2)
        이유 :: 매번 방문하지 않은 노드 중에 짧은 노드의 번호를 반환 해야하기 떄문에 O(V)가 되고 현재 노드와 연결된 노드르 매번 확인하기 때문
    1.1차원 리스트 설정
    2.단계마다"방문하지 않은 노드 중 최단거리가 짧은 노드 선택을 위해 매 단계마다
      1차원 리스트의 모든 원소를 확인(순차 탐색)"
    3.노드 번호를 인덱스로 접근하기위해 array(노드갯수+1)


'''
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미

#노드의 개수.간선의 개수 입력받기
print("노드 개수 간선의 개수 : ")
n,m = map(int, input().split())
#시작 노드 입력
print("시작 노드 입력")
start = int(input())
#각 노드마다 간선 정보 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 판단하는 리스트
visited = [False]*(n+1)
#최단거리 저장 소
distance = [INF]*(n+1)

#모든 간선 정보 입력
for _ in range(m):
    #a노드에서 b노드 까지 가는 비용 C
    print("a b c(a노드에서 b노드 까지 가는 비용 C) : ")
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

#방문하지 않은 노드 중에 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]]= j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 잛은 노드를 꺼내어, 방문 처리
        now = get_smallest_node()
        visited[now]=True
        #현재 노드와 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]]= cost

dijkstra(start)

#모든 노드로 가기 위해 최단거리 출력
for i in range(1,n+1):
    #도달할 수 없는경우 INFINITY출력
    if distance[i] == INF:
        print( "INFINITY", end=" ")
    else:
        print(distance[i],end=" ")

print()

## 내일은  구현은 좀 어렵지만 빠르게 동작하는알고리즘 구현해보기~~!!