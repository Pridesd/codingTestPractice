import sys

n = input()
count1 = []
count0 = []
if (len(n) == 1):
    print(0)
else:
    c = n[0]
    for i in n[1:]:
        if c[0] == i:
            c += i
        else:
            if (c[0] == '1'):
                count1.append(c)
            else:
                count0.append(c)
            c = i
    if (c[0] == '1'):
        count1.append(c)
    else:
        count0.append(c)

    print(min(len(count0), len(count1)))
