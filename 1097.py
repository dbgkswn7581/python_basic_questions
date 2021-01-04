arr = []
b = []
for i in range(19):
    a = input()
    for j in a:
        if j == '0':
            b.append(0)
        elif j == '1':
            b.append(1)
    arr.append(b)
    b = []


def rever(x,y):
    for i in range(19):
        if arr[x-1][i] == 1:
            arr[x-1][i] = 0
        else:
            arr[x-1][i] = 1
        if arr[i][y-1] == 1:
            arr[i][y-1] = 0
        else:
            arr[i][y-1] = 1

m = int(input())
for p in range(m):
    x,y = map(int, input().split())
    rever(x,y)


for i in arr:
    for j in range(19):
        print(i[j], end=' ')
    print()