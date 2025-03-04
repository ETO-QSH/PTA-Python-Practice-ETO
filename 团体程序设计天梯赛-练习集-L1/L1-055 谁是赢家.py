a, b = map(int, input().split())
l = list(map(int, input().split()))

if l.count(0) == 3:
    print(f'The winner is a: {a} + 3')
elif l.count(1) == 3:
    print(f'The winner is b: {b} + 3')
else:
    if a > b:
        print(f'The winner is a: {a} + {l.count(0)}')
    if a < b:
        print(f'The winner is b: {b} + {l.count(1)}')
