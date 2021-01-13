'''
    상하좌우 방향 이동
    시작 좌표 == (1,1)
    N*N 지도
    [R,L,U,D]존재 오른쪽,왼쪽,위,아래
    지도를 벗어나면 이동 무시
    input
        N입력
        이동경로 입력
    output
        도착지 좌표 출력
'''
import time
n = int(input())
moves = input().split()
x,y= 1,1

start = time.time()
## 방법 1
for move in moves:
    if move == 'U':
        x-=1
        if x<1:
            x+=1
    elif move == 'D':
        x+=1
        if x>n:
            x-=1
    elif move == 'L':
        y-=1
        if y<1:
            y+=1
    elif move == 'R':
        y+=1
        if y>n:
            x-=1
    else:
        continue

print(x,y)
end = time.time()
print(end-start)

#방법 2
move_type = ['R','L','U','D']
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = dx[i]
            ny = dy[i]
        if nx<1 or nx>n or ny<1 or ny>n:
            continue
        x +=nx
        y +=ny
print(x,y)
