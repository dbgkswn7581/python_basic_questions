a = int(input())
b = 0
c = 0
d = 1

while True:
    b += d
    c += 1
    d += 1
    if b == a:
        print(c)
        break