Ah, Bh = map(int, input().split())
At, Bt = Ah, Bh

_ = input()

while min(Ah, Bh) >= 0:
    a, b, c, d = map(int, input().split())
    h = a + c
    if h == b == d:  pass
    elif h == b: Ah -= 1
    elif h == d: Bh -= 1
    if Ah < 0: print(f'A\n{Bt-Bh}')
    if Bh < 0: print(f'B\n{At-Ah}')
    