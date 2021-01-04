w,h = map(int, input().split())

a = [] #격자판
b = []
for i in range(w):
    for j in range(h):
        b.append(0)
    a.append(b)
    b = []

n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        k = y-1
    elif d == 1:
        k = x-1

    for j in range(l):
        if d == 0:
            a[x-1][k] = 1
            k += 1
        elif d == 1:
            a[k][y-1] = 1
            k +=1


for i in a:
    for j in range(h):
        print(i[j], end=' ')
    print()
