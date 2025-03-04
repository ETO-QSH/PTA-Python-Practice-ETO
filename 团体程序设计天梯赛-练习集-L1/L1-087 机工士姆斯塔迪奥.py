n, m, q = map(int, input().split())

x, y = [1] * n, [1] * m

for i in range(q):
    a, b = input().split()
    if a == "0": x[int(b) - 1] = 0
    else: y[int(b) - 1] = 0

print(sum(x) * sum(y))
