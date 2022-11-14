n = input().split('-')
minusNum = []
for i in n:
    index = i.find("+")
    if index != -1:
        plus = i.split("+")
        sum = 0
        for j in plus:
            sum += int(j)
        minusNum.append(sum)
    else:
        minusNum.append(int(i))
start = minusNum.pop(0)
for i in minusNum:
    start -= i
print(start)
