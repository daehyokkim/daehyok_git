'''
    2021.01.15
    음료수 얼려 먹기
    N*M크기의 얼음 틀이 있다.
    뚫린 부분 : 0 칸막이 부분 : 1
    0은 상하좌우로 연결되어 있음
    이때 틀 모양에 따라 생성되는 아이스크림의 갯수를 구하는 프로그램 구현
    1<=N,M<=1000
    input
        n m 입력
        틀 생성
    output
        생성 되는 얼음 갯수

'''
def dfs(x,y):
    #좌표를 벗어나면 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #좌표(x,y)가 뚤린 부분인지 확인 하기
    if graph[x][y] == 0:
        graph[x][y]=1
        #상하좌우판별
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m = map(int,input().split())
graph = []
result = 0
'''
초기 구현
    n=4 m=5입력
    for n in range(n):
        graph.append(list(map(int,input())))
    입력시
    for i in range(n):
    print("n의 값 :",n,)
    for j in range(m):
        if dfs(i,j)==True:
            result +=1
    에서 n의 값이 3이 되어 출력 됨
     -2021.01.19 해결-
        --> 첫번째 for 문이 끝날때 n = 3이란 값을 가지고 끝이 나기때문에 다음 for문에서
        range(n)값은 0~2까지 만 반복하기 때문
    
'''
for i in range(n):
    graph.append(list(map(int,input())))

print(graph)
#연결된 구멍 확인 후 얼음 갯수 증가
for i in range(n):
    print("n의 값 :",n,i)
    for j in range(m):
        if dfs(i,j)==True:
            result +=1

print(result)
print(graph)
