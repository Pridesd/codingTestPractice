result = 0
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()

for i in range(n):
    x = a[i]
    y = max(b)
    b.pop(b.index(max(b)))
    result += (x*y)
print(result)
