# import sys

# result = []
# n = int(sys.stdin.readline())
# list = list(map(int, sys.stdin.readline().split()))

# for i in range(n-1):
#     num = list[i]
#     for j in range(i+1, n):
#         if num < list[j]:
#             result.append(list[j])
#             break
#         if j == n-1:
#             result.append(-1)
#             break
# result.append(-1)

# for i in result:
#     print(i, end=" ")
# print()
# 시간초과 O(n^2)


# 스택을 인덱스로 사용하여 문제풀이
import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

stack = [0]
result = [-1] * n

stack.append(0)
for i in range(1, n):
    while stack and list[stack[-1]] < list[i]:
        result[stack.pop()] = list[i]
    stack.append(i)

print(*result)
