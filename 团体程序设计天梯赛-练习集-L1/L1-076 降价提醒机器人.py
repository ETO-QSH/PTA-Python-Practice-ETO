a, b = map(int, input().split())

for i in range(a):
    c = float(input())
    if c < b:
        print(f'On Sale! {c}')
