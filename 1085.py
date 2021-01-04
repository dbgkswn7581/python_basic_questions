x,y,z,w=map(int,input().split())

num1 = x*y*z*w
num2 = num1/1024/1024/8
print("%.1f MB" %num2)
