import sys

n = int(sys.stdin.readline())
count = 0
for i in range(1, n+1):

    if (len(str(i)) <= 2):
        count += 1
    else:
        i = str(i)
        term = int(i[1]) - int(i[0])
        for j in range(1, len(i)):
            if (int(i[j])-int(i[j-1]) != term):
                count -= 1
                break
        count += 1

print(count)
