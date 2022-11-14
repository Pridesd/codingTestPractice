n = int(input())
r = []
for i in range(n):
    r.append(int(input()))
r.sort()
m = 0
j = n
for i in r:
    m = max(i*j, m)
    j -= 1
print(m)
