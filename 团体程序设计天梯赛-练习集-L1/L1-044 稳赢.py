n = int(input())
c = 0
while True:
    s, c = input(), c + 1
    if s == 'End': break
    elif c % (n + 1) == 0: print(s)
    else:
        if s == 'ChuiZi': print('Bu')
        elif s == 'JianDao': print('ChuiZi')
        elif s == 'Bu': print('JianDao')
        else: continue
