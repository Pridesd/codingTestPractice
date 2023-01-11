from collections import deque


def solution(maps):
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]

    queue = deque()
    queue.append([0, 0])

    while queue:
        now = queue.popleft()
        for i in range(4):
            nextx = now[0] + mx[i]
            nexty = now[1] + my[i]

            if (nextx < len(maps) and nexty < len(maps[0]) and maps[nextx][nexty] != 0):
                if (maps[nextx][nexty] == 1):
                    maps[nextx][nexty] = maps[now[0]][now[1]] + 1
                    queue.append([nextx, nexty])
    if (maps[len(maps)-1][len(maps[0])-1] == 1):
        return -1
    else:
        return maps[len(maps)-1][len(maps[0])-1]
    return answer
