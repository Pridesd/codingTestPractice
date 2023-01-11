numList = []
i = 1
n = int(input())
while True:
    if str(i).find('666') != -1:
        numList.append(i)
    if (len(numList) == n):
        print(numList[n-1])
        break
    i += 1

# numList = []
# i = 1
# while True:
#     if str(i).find('666') != -1:
#         numList.append(i)
#     if (len(numList) == 10000):
#         break
#     i += 1
# n = int(input())
# print(numList[n-1])

# numList = []

# for i in range(1, 9999666):
#     if str(i).find('666') != -1:
#         numList.append(i)

# n = int(input())
# print(numList[n-1])
