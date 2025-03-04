a, b = map(float, input().split())

m = a / (b ** 2)
print(f'{m:.1f}')

if m > 25: print('PANG')
else: print('Hai Xing')
