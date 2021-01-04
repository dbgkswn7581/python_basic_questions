n = int(input())
arr = []
for i in range(0,19):
    arr.append([])
    for j in range(0,19):
        arr[i].append(0)

for i in range(n):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1


for i in range(0, 19):
    for j in range(0, 19):
        print(arr[i][j], end=" ")

    print("")
