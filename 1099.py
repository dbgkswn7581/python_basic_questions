a = []

for i in range(10):
    b = list(map(int, input().split()))
    a.append(b)

x = 1
y = 1

while True:
    if a[x][y] == 2:
        a[x][y] = 9
        break
    elif a[x][y] == 1:
        break
    elif a[x][y+1] == 2:
        a[x][y] = 9
        a[x][y+1] = 9
        break
    elif a[x][y+1] == 0:
        a[x][y] = 9
        y += 1
    elif a[x+1][y] == 0:
        a[x][y] = 9
        x += 1
    elif a[x+1][y] == 2:
        a[x][y] = 9
        a[x+1][y] = 9
        break
    elif a[x][y+1] == 1 and a[x+1][y] == 1:
        a[x][y] = 9
        break

for i in a:
    for j in range(10):
        print(i[j], end=' ')
    print()