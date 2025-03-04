a, b = map(int, input().split())

for i in range(b):
    n = input()
    n = n.replace('n', '1')
    n = n.replace('y', '0')
    print(int(n, 2) + 1)
    