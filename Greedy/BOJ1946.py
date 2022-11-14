# t = int(input())
# result = []
# for i in range(t):
#     score = []
#     count = 0
#     n = int(input())
#     for j in range(n):
#         score.append(list(map(int, input().split())))
#     score.sort(reverse=True)
#     for j in score:
#         for k in range(score.index(j)+1, len(score)):
#             if j[1] > score[k][1]:
#                 count -= 1
#                 break
#         count += 1
#     result.append(count)
# for i in result:
#     print(i)
# 시간 초과 오류(중첩 for 때문에 시간초과 발생한듯)

# t = int(input())
# for i in range(t):
#     score = []
#     count = 0
#     n = int(input())
#     for j in range(n):
#         score.append(list(map(int, input().split())))
#     score.sort()
#     m = score[0][1]
#     count += 1
#     for j in range(1, n):
#         if m > score[j][1]:
#             m = score[j][1]
#             count += 1
#     print(count)
# 이거도 시간초과 ㅜ

import sys

t = int(sys.stdin.readline())
for i in range(t):
    score = []
    count = 0
    n = int(sys.stdin.readline())
    for j in range(n):
        score.append([int(x) for x in sys.stdin.readline().split()])
    score.sort()
    m = score[0][1]
    count += 1
    for j in range(1, n):
        if m > score[j][1]:
            m = score[j][1]
            count += 1
    print(count)
