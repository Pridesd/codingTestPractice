import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    count = num.pop(0)
    total = 0
    for j in range(count-1):
        for k in range(j+1, count):
            total += math.gcd(num[j], num[k])
    print(total)
