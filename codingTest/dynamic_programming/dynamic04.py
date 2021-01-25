'''
    2021.01.25
    효율적인 화폐 구성
    n가지 종류의 화페가 있을때 그 가치의 합이 M원으로 만들 수 있는
    최소한의 화폐 개수를 구하여라, 단 존재하지 않을 때 -1을 출력
    1<=100,M<=10000
    input
    N,M
    N개의 화폐입력
    output
    최소화폐 갯수
'''
n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(int(input()))
dp = [10001]*(m+1)
dp[0]=0

for i in range(n):
    for j in range(array[i],m+1):
        if dp[j-array[i]] != 10001:
            dp[j] = min(dp[j],dp[j-array[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
