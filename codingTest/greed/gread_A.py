"""n=data_cnt, m=plus_cnt, k=addnum_cnt"""
import time
"""ex) 5 8 3
       2 4 5 4 6  46
"""
"""
    큰수의 법칙
    N == 배열크기, M == 덧셈횟수 K == 같은인덱스가 연속할 수 있는 횟수
    1Line == N M K
"""

n,m,k = map(int,input().split())
print(n,m,k)
data = list(map(int,input().split(" ")))

data.sort()
first=data[n-1]
second=data[n-2]
sum = 0
cnt =0
start = time.time()

while True:
    for k in range(k):
        if m == 0:
            break
        sum += first
        m -=1
        if m == 0:
            break
    if m == 0:
        break
    sum +=second
    m-=1
print(sum)
end = time.time()

print(end-start)

n,m,k = map(int,input().split())
print(n,m,k)
data = list(map(int,input().split(" ")))

data.sort()
first=data[n-1]
second=data[n-2]
sum = 0
cnt =0

start1 = time.time()
count = m // (k+1) * k
count += m % (k+1)

result = 0
result +=count * first
result+=(m-count)*second

print(result)
end1 = time.time()


print(end1-start1)

