'''
    1이 될 때까지
    조건 1 N에서 1을 뺀다.
    조건 2 N을 K로 나눈다.

'''

n,m =map(int,input().split())
cnt = 0
while True:
    if n%m == 0:
        n/=m
        cnt+=1
    else:
        n-=1
        cnt+=1

    if n ==1:
        break
print(cnt)

