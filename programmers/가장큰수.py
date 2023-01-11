# from itertools import permutations

# def solution(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = str(numbers[i])
#     return str(max(list(map(int, map(''.join, permutations(numbers, len(numbers)))))))
# 시간초과

from itertools import permutations


def solution(numbers):
    answer = ''
    numbers.sort(reverse=True)
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(reverse=True)
    for i in numbers:
        answer += i
    return answer


print(solution([3, 30, 34, 5, 9]))
