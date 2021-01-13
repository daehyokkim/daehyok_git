'''
    게임 개발
   1.현재 위치에서 현재 방향을 기준으로 왼쪽 방향 부터 차례대로 갈 곳을 정한다.
   2.캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재시,
        왼쪽방향으로 회전 후 왼쪽으로 한칸 전진.
     그렇지 않다면
        왼쪽 방향으로 회전만 하고 정지 후 1단계
    3.만약 네 방향이 이미 가본 곳 이거나 바다로 되었다면,
        바라보는 방향을 유지, 1칸 뒤로 이동 후 1번 수행
        but 뒤가 바다라면 정지

    input
    MAP의 크기 입력 N*M : N M
    캐릭터 시작 좌표와 바라보는 방향 입력 (row,col),뱡향(북-0,동-1,남-2,서-3)-->바라보는 방향 기준 왼쪽을 보기 -1 : row col 뱡향
        북
    서       동
        남
    주어진 맵중 육지(0)와 바다(1)설계 단.태두리는 모두 바다
    처음 캐릭터는 항상 육지

    output
    첫쨰 줄에 이동을 바친 후 캐릭터가 방분한 칸 수 출력.
'''

n,m= map(int,input().split())
x,y,direction = map(int,input().split())

#방문한 위치를 저장하기 위한 맵을 생성 0초기화
d =[[0]*m for _ in range(n)]
d[x][y]=1
arry = []

for n in range(n):
    arry.append(list(map(int,input().split())))
#북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction = 3 #북쪽을 바라볼 시 왼쪽으로 90회전 해야하기 떄문에 3==서

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전 후 정면이 가보지 않은 곳이면 이동
    if d[nx][ny] == 0 and arry[nx][ny] != 1:
        d[nx][ny] = 1
        x=nx
        y=ny
        count +=1
        turn_time = 0
        continue
    #정면이 가보지 않은 칸이 없거나 바다인경우
    else:
        turn_time+=1
    #네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x -dx[direction]
        ny = y -dy[direction]
        #뒤로 갈 수 있는 경우 이동
        if arry[nx][ny]!=1:
            x = nx
            y = ny
        #뒤에 바다가 막힌 경우
        else:
            break
        turn_time=0

print(count)


