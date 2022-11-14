n = int(input())
maxScore = 0
for i in range(n):
    a, d, g = map(int, input().split())
    score = a * (d+g)
    if a == (d+g):
        score *= 2
    maxScore = max(maxScore, score)
print(maxScore)
