a = input()
for i in range(5):
    b = int(a[i]) * (10 ** (4-i) )
    print("[%d]" %b)