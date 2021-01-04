x,y,z=map(int,input().split())

num1 = x*y*z
num2 = num1/1024/1024/8
print("%.2f MB" %num2)
