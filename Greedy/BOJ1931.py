n = int(input())
start = []
count = 0
current = []
for i in range(n):
    t = list(map(int, input().split()))
    start.append(t)

# 시작시간 기준으로 정렬
start.sort(key=lambda x: x[0])
# 종료시간 기준으로 정렬
start.sort(key=lambda x: x[1])

endTime = start[0][1]
count += 1
for i in range(1, n):
    if endTime <= start[i][0]:
        endTime = start[i][1]
        count += 1
print(count)
