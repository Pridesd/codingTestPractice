import sys

n, m = map(int, sys.stdin.readline().split())
board = []
result = []
for i in range(n):
    board.append(list(sys.stdin.readline())[:m])

for i in range(n-7):  # 행
    for j in range(m-7):  # 열
        draw1 = 0
        draw2 = 0
        for k in range(i, i+8):
            for p in range(j, j+8):
                if (k+p) % 2 == 0:
                    if board[k][p] != "B":
                        draw1 += 1
                    if board[k][p] != "W":
                        draw2 += 1
                else:
                    if board[k][p] != "W":
                        draw1 += 1
                    if board[k][p] != "B":
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)
print(min(result))
