'''
    2021.01.21
    부품 찾기
    부품 매장에 부품이 n개가 존재한다.
    손님이 m개 종류를 대량 구매하기 위해 찾아왔다.
    이때 매장에 손님이 찾는 m개의 부품이 존재하는지 확인하는 프로그램을 작성하시오.
    n,m<=1,000,000 ---> O(logN)
    input
    n
    n개의 부품 종류
    m
    m개의 부품 종류

    output
    m개의 부품 종류 yes or no (공백으로 출력)
'''
#매장 부품
n = int(input())
store_arry = list(map(int,input().split()))
#손님 부품
m = int(input())
user_arry = list(map(int,input().split()))
user_arry=user_arry[:m]
#정렬
store_arry = sorted(store_arry[:n])

#이진 탐색으로 해결
def binary_search(s_arry,start,end,target):
    if start>end:
        return None
    mid = (start+end)//2

    if s_arry[mid] == target:
        return mid

    elif s_arry[mid] > target:
        return binary_search(s_arry,start,mid-1,target)
    else:
        return binary_search(s_arry,mid+1,end,target)

for i in user_arry:
    result = binary_search(store_arry,0,n-1,i)
    if result == None:
        print("No",end=" ")
    else:
        print("Yes",end=" ")

#set자료형으로도 가능 하다
print()
n = int(input())
arry = set(map(int,input().split()))
m = int(input())
user = list(map(int,input().split()))
user = user[:m]

for i in user:
    if i in arry:
        print("Yes",end=" ")
    else:
        print("No",end=" ")