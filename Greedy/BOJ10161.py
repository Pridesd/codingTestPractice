a = 0
b = 0
c = 0

n = int(input())

a = n//300
n %= 300
b = n // 60
n %= 60
c = n // 10
n %= 10

if n == 0:
    print(a, b, c, sep=" ")
else:
    print(-1)
