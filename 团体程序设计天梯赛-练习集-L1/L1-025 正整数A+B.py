a, b = input().split(' ', 1)

error = False

if a.isdigit() and int(a) in range(1, 1001):
    a = int(a)
else:
    a = '?'
    error = True
if b.isdigit() and int(b) in range(1, 1001):
    b = int(b)
else:
    b = '?'
    error = True

print(f'{a} + {b} = {"?" if error else a + b}')
