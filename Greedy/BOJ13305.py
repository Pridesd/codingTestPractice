n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

minPrice = p[0]
result = 0

for i in range(n-1):
    minPrice = min(minPrice, p[i])
    result += (minPrice*d[i])
print(result)
