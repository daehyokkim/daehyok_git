'''
    2021.01.21
    떡볶이 떡 만들기
    매장의 떡볶이 떡은 길이가 일정하지 않다.
    하지만 한봉지에 들어가는 떡의 총길이는 절단기로 잘 맞줘준다.
    절단기 높이(h)를 지정하면  h보다 긴 떡은 잘라진다.
    이때 잘린 자투리 떡은 손님이 가져간다.
    이를 바탕으로 손님이 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정 할 수 있는
    높이의 최댓값을 구하는 프로그램을 작성하시오
    input
        N(떡의 개수) M(요청한 떡의 길이)
        떡의 개별 높이
        (떡의 높이의 총합은 항상 M이상이므로 손님이 필요한 양만큼 떡을 사갈 수 있다.)
        높이는 10억보다 작거나 같고 N<=1,000,000 M<=2,000,000
    output
        적어도 M만큼의 떡을 집에 가져가기 위해 절단에 설정할 수 있는 높이의 최댓값
'''
n,m = map(int,input().split())
arry = list(map(int,input().split()))
arry = arry[:n]
end = max(arry)
start = 0
result = 0
while start <= end:
    mid = (start+end)//2
    sum = 0
    for i in arry:
        if i > mid:
            sum += i - mid

    print(sum)
    if sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid +1

print(result)