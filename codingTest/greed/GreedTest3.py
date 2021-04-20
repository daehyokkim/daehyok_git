#문자열 뒤집기
#1과0으로 이루어진 문자열 S를 하나이상의 연속적인 숫자를 0은1로 1은 0으로 뒤집을떄
#최소로 뒤집어 같은 숫자가 도록하시오.

#00100110
import sys

input = sys.stdin.readline()
data = input
cntOne = 0
cntTwo = 0
num = data[0]
for i in range(1,len(data)):
    if num != data[i]:
        if data[i] == '1':
            cntOne +=1
            num=data[i]
        else:
            cntTwo +=1
            num=data[i]

result = min(cntOne,cntTwo)
print(result)




data = input()
cntOne = 0
cntTwo = 0

if data[0] == '1':
    cntOne += 1
else:
    cntTwo += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:

        if data[i + 1] == '1':
            cntOne += 1
        else:
            cntTwo += 1

result = min(cntOne, cntTwo)
print(result)
