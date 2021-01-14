'''
 문자열 재정렬 하기
 조건 : 입력한 문자열을 알파벳을 오름차순으로 정렬하고 숫자를 모두 더하여 마지막에 입력하기
 input
  K1K2J3N4K5J4V3F

  output
  알파벳오름차순 숫자더하기
'''

data = input()
result = []
sum = 0
for i in data:
    #해당 문자가 문자인지 아닌지 판단. 문자:T 정수:F
    if i.isalpha():
        result.append(i)
    else:
        sum+=int(i)

result.sort()
if sum !=0:
    result.append(str(sum))
print(''.join(result))

