'''
    2021.01.19
    두 배열의 원소 교체
    N개의 원소로 이루어지 A,B의 배열을 최대 k번 바꿔치기 연산을 허용한다.
    이때 A배열의 모든 원소의 합이 최대가 되도록 하는 것
    모든 원소는 10,000,000보다 작다 ---> 계수 정렬은 비효율적임
    원수의 갯수는 100,000개보다 작아야한다 ---> O(NlogN)구현
    input
     n k
     A배열 n개 생성
     B배열 n개 생성

     output
     A배열의 최댓값
'''
'''
    A배열을 오름차순 정렬
    B배열을 내림차순 정렬
    for K번 수행
        A,B배열 SWAP
'''

n,k = map(int,input().split())
arry_A = list(map(int,input().split()))
arry_B = list(map(int,input().split()))

#배열안에 원소 갯수를 n개로 맞춤
arry_A=arry_A[:n]
arry_B=arry_B[:n]

#A는 오름차순 B는 내림차순 정렬
arry_A = sorted(arry_A)
arry_B = sorted(arry_B,reverse=True)
print(arry_A,arry_B)

for i in range(k):
    #두 배열중 가장 큰값을 A로 SWAP
    if arry_A > arry_B:
        arry_A[i],arry_B[i] = arry_B[i],arry_A[i]
    #A는 올림 B는 내림차순 이기 때문에 전부 반복 필요 X
    else:
        break
result = 0
for i in arry_A:
    result+=i

print(result)
