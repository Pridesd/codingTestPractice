# n = int(input())

# stack = []

# for i in range(n):
#     e = list(input().split())
#     e1 = e[0]
#     if e1 == "push":
#         stack.insert(0, int(e[1]))
#     elif e1 == "pop":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop(0))
#     elif e1 == "size":
#         print(len(stack))
#     elif e1 == "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     elif e1 == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[0])
# input을 쓰면 시간 초과 sys 사용해야 함

import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    e = sys.stdin.readline().split()
    e1 = e[0]
    if e1 == "push":
        stack.insert(0, int(e[1]))
    elif e1 == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    elif e1 == "size":
        print(len(stack))
    elif e1 == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif e1 == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
