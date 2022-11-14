# n = int(input())
# count = 0

# count += (n//5)
# n %= 5
# count += (n//3)
# n %= 3
# if (n == 0):
#     print(count)
# else:
#     print(-1)

# n = int(input())
# count = 0
# if n % 3 == 0:
#     if n % 5 == 0:
#         count += (n//5)
#     else:
#         count += (n//3)
# else:
#     while True:
#         if n % 5 == 0:
#             count += (n//5)
#             break
#         if n % 3 == 0:
#             count += (n//3)
#             break
#         if n < 5:
#             if n < 3:
#                 count = -1
#                 break
#             else:
#                 n -= 3
#                 count += 1
#         else:
#             n -= 5
#             count += 1
# print(count)

n = int(input())
count = 0

while n > 0:
    if n % 5 == 0:
        count += (n//5)
        n /= 5
    else:
        n -= 3
        count += 1
if n == 0:
    print(count-1)
else:
    print(-1)
