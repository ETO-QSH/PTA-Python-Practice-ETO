y, n = map(int, input().split())

if (y, n) == (1, 2):
    print('0 0001')
else:
    m = 0
    while True:
        y, m = y + 1, m + 1
        ys = str(y).zfill(4)
        ll = len(set([i for i in ys]))
        if ll == n:
            print(m, str(y).zfill(4))
            break
    