x,y,z=map(int,input().split())

l = 0

for i in range(x):
    for j in range(y):
        for k in range(z):
            print("%d %d %d" %(i,j,k))
            k+=1
            l+=1
        j+=1
    i+=1

print(l)