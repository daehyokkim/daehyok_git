#스텍 생성
stack = []

stack.append(1)
stack.append(5)
stack.append(10)
stack.pop()
stack.append(20)
print(stack)

#큐 생성
from collections import deque
queue = deque()
queue.append(20)
queue.append(30)
queue.append(4)
queue.popleft()
queue.append(40)
print(list(queue))
print(queue)

#재귀함수 펙토리얼 예제
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
