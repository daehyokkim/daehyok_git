'''
 2021.01.19
 대표적인 기본 정렬 문제 풀이
'''

#위에서 아래로
#오름차순으로 정렬하기~
n = int(input())
arry=[]
for i in range(n):
    arry.append(int(input()))

arry =sorted(arry,reverse=True)
for i in arry:
    print(i,end=' ')
