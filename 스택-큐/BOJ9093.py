import sys

n = int(sys.stdin.readline())

for i in range(n):
    word = sys.stdin.readline().split()
    for j in word:
        for k in range(len(j)-1, -1, -1):
            print(j[k], end="")
        print(end=" ")
    print()
