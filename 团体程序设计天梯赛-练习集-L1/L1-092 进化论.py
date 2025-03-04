for i in range(int(input())):
    a, b, c = map(int, input().split())
    if c == (a * b): print('Lv Yan')
    elif c == (a + b): print('Tu Dou')
    else: print('zhe du shi sha ya!')
