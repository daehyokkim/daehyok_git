'''
    2021.01.21
    dynamic_porgramming 기초 코딩
    대표적인 문제인 피보나치를 구현 해보기
    f(N) = f(n-1)+(fn-2)
    단 f(1)=1,f(2)=1이다.
     1 1 2 3 8 ...
'''
#Top-Down방식
#memoization하기 위한 리스트 초기화
#재귀함수 깊이 오류 발생 시 sys 라이브러리에 sys.setrecursionlimit()사용시 완하는 가능하다.
chaching = [0]*100

def top_down(x):
    if x == 1 or x==2:
        return 1
    if chaching[x] != 0:
        return chaching[x]
    chaching[x] = top_down(x-1)+top_down(x-2)
    return chaching[x]
num=top_down(99)
print(num)

#Bottom_Up 방식
dp = [0]*100

dp[1] = 1
dp[2] = 1
n=99

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[-1])