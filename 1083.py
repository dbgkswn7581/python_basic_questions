a=int(input())
i=1

while i<=a:

    if i%3==0:
        l=len(str(i))
        print("X"*l,end=(" "))

    elif i%3!=0 :
        print(i,end=(" "))

    i+=1