list = []
while True:
    i = int(input())
    if i != 0:
        list.append(i)
    elif i == 0:
        break
print(*list)