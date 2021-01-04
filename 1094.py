a = int(input())
b = input().split()
arr = []

for i in range(a):
    arr.append(b[i])

arr.reverse()

for i in range(a):
    print(arr[i], end=' ')