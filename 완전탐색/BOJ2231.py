import sys

n = int(sys.stdin.readline())
result = 0
for i in range(1, n+1):
    s = i
    m = i
    while m != 0:
        s += (m % 10)
        m = m // 10
    if s == n:
        result = i
        break
print(result)
