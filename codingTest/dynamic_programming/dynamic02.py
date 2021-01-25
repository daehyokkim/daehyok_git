'''
    2021.01.25
    개미 전사
    일직선으로 이어져 있는 식량창고에서 식량을 훔치려한다.
    이때 인접한 식량창고가 공격할 수 없다.
    그렇다면 최소 한 칸 이상 떨어진 식량창고를 약탈할 때 최대값을 구하시오.
    input
    n#창고갯수
    [2,3,4,6]//창고안의 식량 갯수
    output
    9최댓값
'''
n = int(input())
array = list(map(int,input().split()))
array = array[:n]

dp = [0]*100
dp[0]=array[0]
dp[1]=max(array[0],array[1])
for i in range(2,n):
    dp[i]=max(array[i-1],array[i-2]+array[i])

print(dp[i])

