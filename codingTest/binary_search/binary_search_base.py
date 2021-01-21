#이진 탐색 구현해보기
#재귀함수를 사용하여 구현
arry = [0,19,49,5,2,7,4,10,20,30,50]

#오름차순으로 배열 정렬
arry = sorted(arry)
print(arry)
#시작점,끝점,중간점 표시
start = 0
end = len(arry)-1

#재귀함수 사용
def binary_search(arry,start,end,value):

    #값이 존재하지 않을때 
    if start>end:
        return None
    #중간값 설정
    mid = (end+start)//2
    print(end, start,mid)
    #값을 찾으면 함수 종료
    if arry[mid] == value:
        return mid
    #중간값이 답보다 크다면?
    elif arry[mid] > value:
        return binary_search(arry,start,mid-1,value)
    # 중간값이 답보다 작다면?
    else:
        return binary_search(arry,mid+1,end,value)

index=binary_search(arry,start,end,9)
print('정답이 위치한 인덱스',index)
if index != None:
    print('해당값 찾음')
else:
    print("존재하는 값이 아닙니다.")
"""
import sys
input_type = sys.stdin.readline().strip()
"""