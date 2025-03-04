k = input()

a, b = map(int, k.split(':'))

if a in range(12, 24):
    if a == 12 and b == 0:
        print(f'Only {k}.  Too early to Dang.')
    elif b == 0:
        print('Dang'*(a-12))
    else:
        print('Dang'*(a-11))
else:
    print(f'Only {k}.  Too early to Dang.')
    