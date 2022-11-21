import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
count = [0]*(max(data)+1)
result = [-1]*n
stack = []

for i in data:
    count[i] += 1
stack.append(0)
for i in range(1, n):
    while stack and count[data[stack[-1]]] < count[data[i]]:
        result[stack.pop()] = data[i]
    stack.append(i)
print(*result)
