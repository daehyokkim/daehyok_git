'''
   곱하기 혹은 더하기
   왼쪽부터 차례대로 + or *을 실행하여 가장 큰 수를 뽑는다.
   단 0 or 1인 경우 +를 실행하는 것이 효율적이다.
    input
        정수
    output
        최댓값
'''

numbers = input()
result = int(numbers[0])
for i in range(len(numbers)):
    num = int(numbers[i])
    if result!=0 and num != 0 and num != 1 :
        result *= num
    else:
        result +=num

print(result)