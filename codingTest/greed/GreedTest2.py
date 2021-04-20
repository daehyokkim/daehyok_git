#곱하기 혹은 더하기
# 각자리수가0~9까지의 문자열 s가 주어지고 왼쪽부터 오른쪽 순으로 해당 값을
# + or *을 이용해 가장 큰 값을 구하시오.
#단 연산자는 우선순위없이 왼쪽에서 오른쪽으로 차례대로 계산한다.

number = input()
number = sorted(number)
result = 0

for i in range(1,len(number)):
    num =int(number[i])
    if  result <= 1 or num <= 1:
        result += num

    else:
        result *= num

print(result)
