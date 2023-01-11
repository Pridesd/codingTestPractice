num = set()
for i in range(1, 10001):
    n = i
    selfNum = i
    while (n != 0):
        selfNum += (n % 10)
        n = n//10
    if (selfNum > 10000):
        continue
    else:
        num.add(selfNum)

for i in range(1, 10001):
    if (i not in list(num)):
        print(i)
