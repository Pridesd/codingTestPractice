import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    count = 1
    for j in range(n):
        if (li[i][0] < li[j][0] and li[i][1] < li[j][1]):
            count += 1
    print(count, end=" ")
