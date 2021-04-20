### 모험가 길드
# 공포도가 x인 모험가는 반드시 x명 이상으로 길드를 구성해야한다.

#input
#첫째 즐에 모험가의 수 N이 주어집니다.(100,000)
#둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

#output
#여행을 떠날 수 있는 그룹의 수 최댓값

n = int(input())
data = list(map(int,input().split(" ")))
data=data[:n]
data=sorted(data)
count =0
result = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count=0

print(result)

