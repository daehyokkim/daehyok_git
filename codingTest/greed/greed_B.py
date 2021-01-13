"""
 숫자 카드 게임
 각 행 중 최소 값을 찾고 그중 가장 큰 값을 출력
   1 312
   2 414
   3 222
"""
import time
'''
st=time.time()
row,col = map(int,input().split())
result=0
for row in range(row):
    card=list(map(int,input().split(" ")))
    if result<min(card):
        result = min(card)

print(result)
et = time.time()
'''
start = time.time()
n,m = map(int,input().split())
result = 0
for n in range(n):
    col = list(map(int,input().split()))
    col = col[:m-1]

    min_v = min(col)

    result = max(result,min_v)
print(result)
end = time.time()
print(end - start)
