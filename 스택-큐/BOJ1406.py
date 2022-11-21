import sys

answer = list(sys.stdin.readline())
answer.pop()
n = len(answer)
m = int(sys.stdin.readline())
now = n

for i in range(m):
    orderList = sys.stdin.readline().split()
    order = orderList[0]
    if order == "L" and now != 0:  # 왼쪽으로 이동
        now -= 1
    elif order == "D" and now != n:  # 오른쪽으로 이동
        now += 1
    elif order == "B" and now != 0:  # 왼쪽 문자 삭제
        answer.pop(now-1)
        now -= 1

    elif order == "P":
        insert = orderList[1]
        answer.insert(now, insert)
        now += 1

for i in answer:
    print(i, end="")
print()
# 시간초과 발생
