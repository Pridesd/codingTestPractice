n = int(input())
num = list(map(int, input().split()))

count = 0
for i in num:
    if i == 2 or i == 3:
        count += 1
        continue
    if i % 2 == 0 or i == 1:
        continue
    for j in range(3, i):
        if i % j == 0:
            count -= 1
            break
    count += 1
print(count)
