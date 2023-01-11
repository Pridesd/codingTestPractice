# import math

# numList = []
# def isPrime(n):
#     if(n == 2 or n == 3):
#         return True
#     if(n == 1 or n % 2 == 0):
#         return False
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         if(n % i == 0):
#             return False
#     return True

# def getNum(num, index, word):
#     newNum = word + num[index]
#     if (int(newNum) not in numList and int(newNum) != 0):
#         numList.append(int(newNum))
#     numCopy = [] + num #리스트의 값을 복사하는 과정
#     numCopy.pop(index)
#     for i in range(len(numCopy)):
#         getNum(numCopy, i, newNum)

# def solution(numbers):
#     num = []
#     primeList = []
#     for i in range(len(numbers)):
#         num.append(numbers[i])
#     for i in range(len(num)):
#         getNum(num, i, "")
#     for i in numList:
#         if(isPrime(i)):
#             primeList.append(i)
#     answer = len(primeList)
#     return answer

import math
primeSet = set()


def isPrime(n):
    if (n == 2 or n == 3):
        return True
    if (n in [0, 1] or n % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if (n % i == 0):
            return False
    return True


def recursive(combination, others):
    if (combination != ""):
        if (isPrime(int(combination))):
            primeSet.add(int(combination))
    for i in range(len(others)):
        recursive(combination+others[i], others[:i] + others[i+1:])


def solution(numbers):
    num = list(numbers)
    recursive("", numbers)
    return len(primeSet)
