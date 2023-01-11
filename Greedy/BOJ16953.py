# a, b = map(int, input().split())
# count = 0
# while b > a:
#     b = str(b)
#     if (b[-1] == '1'):
#         b = b[:len(b)-1]
#         b = int(b)
#         count += 1
#     else:
#         b = int(b)
#         b = b // 2
#         count += 1
# if (b != a):
#     print(-1)
# else:
#     print(count+1)

a, b = map(int, input().split())
count = 0
while b > a:
    b = str(b)
    if (b[-1] == '1'):
        b = b[:len(b)-1]
        b = int(b)
        count += 1
    else:
        if (int(b) % 2 != 0):
            b = int(b)
            break
        b = int(b)
        b = b // 2
        count += 1
if (b != a):
    print(-1)
else:
    print(count+1)
