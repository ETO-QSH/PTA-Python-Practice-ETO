for i in range(int(input())):
    suma, sumb = 0, 0
    a, b = map(int,input().split())
    suma = sum(int(j) for j in str(a))
    sumb = sum(int(j) for j in str(b))
    if a % sumb == 0 and b % suma != 0: print("A")
    elif b % suma == 0 and a % sumb != 0: print("B")
    else: print("A") if a > b else print("B")
