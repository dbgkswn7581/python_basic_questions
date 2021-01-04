a = int(input())
b = input().split()
arr = []

for i in range(a):
    arr.append(int(b[i]))

k = min(arr)

print(k)
