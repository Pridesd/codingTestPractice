import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
card.sort()
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num = card[i] + card[j] + card[k]
            if (num <= m and num >= result):
                result = num

print(result)
