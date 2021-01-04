a,b = map(int, input().split())
b1 = bool(a)
b2 = bool(b)

print(int((b1 == True and b2 == False) or (b1 == False and b2 == True)))

