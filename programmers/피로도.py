def explore(k, dungeons):

    root = []
    if k < 0:
        print("피로도로 탐사 불가")
        return -1
    else:
        for i in range(len(dungeons)):
            if (dungeons[i][0] <= k):
                print("탐사지역", dungeons[i][0], dungeons[i][1])
                root.append(
                    explore(k-dungeons[i][1], dungeons[:i]+dungeons[i+1:]) + 1)
            else:
                return -1
    if (len(root) != 0):
        return max(root)


def solution(k, dungeons):

    return explore(k, dungeons)
