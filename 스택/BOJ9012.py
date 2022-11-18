import sys

n = int(sys.stdin.readline())
for i in range(n):
    stack = []
    result = 0
    data = sys.stdin.readline()
    for j in range(len(data)-1):
        if data[j] == "(":
            stack.insert(0, "(")
        else:
            if len(stack) == 0:
                result = -1
                break
            else:
                stack.pop()
    if len(stack) == 0 and result == 0:
        print("YES")
    else:
        print("NO")
