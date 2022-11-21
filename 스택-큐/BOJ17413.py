data = list(input())

i = 0
start = 0

while i < len(data):
    if data[i] == "<":
        i += 1
        while data[i] != ">":
            i += 1
        i += 1
    elif data[i].isalnum():
        start = i
        while i < len(data) and data[i].isalnum():
            i += 1
        temp = data[start:i]
        temp.reverse()
        data[start:i] = temp
    else:
        i += 1

print("".join(data))
