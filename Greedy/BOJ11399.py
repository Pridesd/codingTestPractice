n = int(input())
p = input().split()
t = 0
total = 0
for i in range(n):
    p[i] = int(p[i])
p.sort()
for i in p:
    t = t + i
    total += t
print(total)
