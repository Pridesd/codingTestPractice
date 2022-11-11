n = int(input())
sum = 0
for i in range(0, n):
    sum += i
    if (sum > n):
        print(i-1)
        break
    elif (sum == n):
        print(i)
        break
