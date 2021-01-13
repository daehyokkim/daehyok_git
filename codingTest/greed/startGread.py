'''
    거스름돈 그리드 알고리즘
     n원을 500,100,50,10원 중 최소 동전 개수 구하기
    단 n원은 항상 10의 배수이다.
'''

N = int(input('N원을 입력하시오(단 N는10의 배수) : '))
money = [500,100,50,10]
cnt = 0
for money in money:
    cnt += N//money
    N%=money

print(cnt)