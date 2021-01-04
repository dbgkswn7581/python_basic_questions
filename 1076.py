a=str(input())

b=ord('a')

while True:
    print(chr(b), end=' ')
    b += 1
    if chr(b) == a:
        print(chr(b))
        break