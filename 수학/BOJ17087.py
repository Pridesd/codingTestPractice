import math


def gcdList(g):
    result = g[0]
    if len(g) == 1:
        return result
    for i in g:
        result = math.gcd(result, i)
    return result


n, s = map(int, input().split())

child = list(map(int, input().split()))
result = []
for i in child:
    result.append(abs(i-s))
print(gcdList(result))
