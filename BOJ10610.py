n = list(input())
n.sort()
k = 1
result = 0
sum = 0
for i in n:
    sum += int(i)

# 각자리수의 합이 3의 배수이면 이 수는 어떤 조합으로 만들던 3의 배수이다!!
if (int(n[0]) != 0 or sum % 3 != 0 or sum == 0):
    print(-1)
else:
    for i in n:
        result += (k * int(i))
        k *= 10
    print(result)
