import sys
import math

# 에라토스체네스의 채 사용


def get_prime_num(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (prime[i]):
            j = 2
            while (i*j <= n):
                prime[i*j] = False
                j += 1
    return prime


arr = get_prime_num(1000000)
while (True):
    n = int(sys.stdin.readline())
    if (n == 0):
        break
    for i in range(3, n, 2):
        if (arr[i] and arr[n-i]):
            print(n, "=", i, "+", n-i, sep=" ")
            break
