a = input()

if len(a) == 4:
    if int(a[:2]) < 22: print('20'+a[:2]+'-'+a[2:])
    else: print('19'+a[:2]+'-'+a[2:])
else: print(a[:4]+'-'+a[4:])
