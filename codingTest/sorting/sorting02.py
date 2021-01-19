# 성적이 낮은 순서로 학생 출력하기
'''
   2021.01.19
    input
     성적이 낮은 학생의 수 n 입력
     학생이름 문자열 a 와 학생 성적 정수 b가 공백으로 구분
     문자열 A길이와 학생의 성적은 100이하 자연수.

    output
     성적이 낮은 순서대로 출력
'''
n = int(input())
arry = []

for i in range(n):
    input_data = input().split(" ")
    arry.append((input_data[0], int(input_data[1])))

arry = sorted(arry, key=lambda arry: arry[1])
print(arry)
for student in arry:
    print(student[0], end=" ")
