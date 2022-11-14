# import sys

# n = int(sys.stdin.readline())

# card = []

# for i in range(n):
#     card.append(int(sys.stdin.readline()))

# card.sort()
# if n == 1:
#     print(0)
# elif n == 2:
#     print(card[0] + card[1])
# else:
#     now = card[0]
#     sum = 0
#     for i in range(n-1):
#         now += card[i+1]
#         sum += now
#     print(sum)
# 문제 오류

# 힙 사용
import sys
import heapq

n = int(sys.stdin.readline())

card = []
result = 0

for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))

if n == 1:
    print(result)
else:
    while len(card) > 1:
        value = heapq.heappop(card) + heapq.heappop(card)
        result += value
        heapq.heappush(card, value)
    print(result)
