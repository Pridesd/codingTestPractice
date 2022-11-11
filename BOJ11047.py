n, k = map(int, input().split())
count = 0
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
for i in range(n):
    count += (k // coin[i])
    k %= coin[i]
print(count)
