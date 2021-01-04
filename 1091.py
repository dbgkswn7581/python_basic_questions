x,y,z,w=map(int,input().split())

for i in range(w-1):
    x = (x*y) + z
print(x)
