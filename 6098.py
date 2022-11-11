maze = []
x = 1
y = 1
for i in range(10):
    row = input().split()
    maze.append(row)
while True:
    if maze[x][y] == "2":
        maze[x][y] = "9"
        break
    maze[x][y] = "9"
    if maze[x][y+1] == "1" and maze[x+1][y] == "1":
        break
    if maze[x][y+1] == "0" or maze[x][y+1] == "2":
        y += 1
    else:
        x += 1

for i in range(10):
    for j in range(10):
        print(maze[i][j], end=" ")
    print()
