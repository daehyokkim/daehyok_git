'''
 2021.01.18
 정렬의 다야한 방법 기초 작성해 보기
'''
#선택 정렬
from time import sleep

list = [1,5,3,9,2,6,8,7,4]
print("선택정렬",list)
for i in range(len(list)):
    min_index = i
    for j in range(i+1,len(list)):
        if list[min_index]>list[j]:
            min_index=j
        list[i],list[min_index] = list[min_index],list[i]

print(list)

#삽입 정렬
list = [1,5,3,9,2,6,8,7,4]
print("삽입정렬",list)
for i in range(1,len(list)):
    for j in range(i,0,-1):
        if list[j] < list[j-1]:
            list[j-1],list[j]=list[j],list[j-1]
        else:
            break
print(list)

#퀵정렬
list = [1,5,3,9,2,6,8,7,4]
print("퀵정렬",list)
def quick_Sort(list,start,end):
    if start >= end:
        return
    pivot = start
    left = start+1
    rigth = end
    while left <= rigth:
        while left <= end and list[pivot] >= list[left]:
            left +=1
        while rigth > start and list[pivot] <= list[rigth]:
            rigth -=1
        if left > rigth:
            list[pivot],list[rigth]=list[rigth],list[pivot]
        else:
            list[left],list[rigth]=list[rigth],list[left]

    quick_Sort(list,start,rigth-1)
    quick_Sort(list,rigth+1,end)

def quick_Sort_Two(list):
    if len(list) <=1:
        return list
    pivot = list[0]
    tail = list[1:]

    left_side = [ x for x in tail if x <= pivot]
    rigth_side = [x for x in tail if x > pivot]

    return quick_Sort_Two(left_side) + [pivot] + quick_Sort_Two(rigth_side)


quick_Sort(list,0,len(list)-1)
print(list)

list = [1,5,3,9,2,6,8,7,4,1,2,1]
print("퀵정렬 2",list)
print(quick_Sort_Two(list))

#계수 정렬
def count_Sort(list):
    count = [0] * (max(list)+1)
    print(count)
    arry=[]
    for i in range(len(list)):
        count[list[i]] +=1

    for i in range(len(count)):
        for j in range(count[i]):
          arry.append(i)
    return arry

print(count_Sort(list))
