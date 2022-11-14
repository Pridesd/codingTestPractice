n = int(input())
c = {}
result = 0
for i in range(n-1):
    child, parent = input().split()
    c[child] = parent

child, parent = input().split()
while child != None:
    if c.get(child) == parent:
        result = 1
        break
    child = c.get(child)
print(result)

# 이건 나중에 풀어보기
