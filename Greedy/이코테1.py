# n, k = map(int, input().split())
# count = 0
# while n > 1:
#     if n % k == 0:
#         n /= k
#     else:
#         n -= 1
#     count += 1
# print(count)

n, k = map(int, input().split())
count = 0

while True:
    target = (n//k)*k  # 이렇게 해서 나눠지는 놈을 바로 찾을 수 있음
    count += (n - target)
    n = target
    n //= k
    if n == 0:
        break
    count += 1

count += (n-1)
print(count)
