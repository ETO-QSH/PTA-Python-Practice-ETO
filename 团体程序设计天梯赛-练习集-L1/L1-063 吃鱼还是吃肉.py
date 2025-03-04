for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        t1 = ['ni li hai!' if b - 130 > 0 else ('duo chi yu!' if b - 130 < 0 else 'wan mei!')][0]
        t2 = ['shao chi rou!' if c - 27 > 0 else ('duo chi rou!' if c - 27 < 0 else 'wan mei!')][0]
    else:
        t1 = ['ni li hai!' if b - 129 > 0 else ('duo chi yu!' if b - 129 < 0 else 'wan mei!')][0]
        t2 = ['shao chi rou!' if c - 25 > 0 else ('duo chi rou!' if c - 25 < 0 else 'wan mei!')][0]
    print(f'{t1} {t2}')
