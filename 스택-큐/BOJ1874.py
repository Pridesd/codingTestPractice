import sys

n = int(sys.stdin.readline())
answer = []
result = []
stack = []

for i in range(n):
    answer.append(int(sys.stdin.readline()))

j = 0
for i in range(1, n+1):
    stack.append(i)
    result.append("+")
    while j < n and answer[j] == stack[-1]:  # -가 붙이면 뒤에서부터 탐색한
        stack.pop()
        result.append("-")
        j += 1
        if len(stack) == 0:
            break

if stack:
    print("NO")
else:
    for i in result:
        print(i)
