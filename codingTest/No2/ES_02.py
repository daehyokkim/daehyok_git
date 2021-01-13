'''
    왕실의 나이트
    나이트가 움직일 수 있는 경우의 수 작성

   1.수평 2 and 수직 1
   2.수직 2 and 수평 1
'''

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]))-int(ord('a'))+1
cnt = 0

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)]

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row<1 or next_row>8 or next_col<1 or next_col>8:
        continue

    cnt +=1

print(cnt)
