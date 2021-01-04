a=int(input())
arr = [[0 for col in range(19)] for row in range(19) ]

for i in range(a):
    x,y = map(int, input().split())

    arr[int(x-1)][int(y-1)] = 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
