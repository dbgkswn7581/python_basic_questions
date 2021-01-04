x,y,z=map(int,input().split())
a = 1
while True:
    if a%x==0 and a%y==0 and a%z==0:
        print(a)
        break
    a +=1