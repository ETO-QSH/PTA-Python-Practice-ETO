import math

N = input()
ls = input().split()
a, b = 0, 1

for item in ls:
    i, j = map(int, item.split("/"))
    a, b = i * b + a * j, b * j
    t = math.gcd(a, b)
    a, b = a // t, b // t

ans = []
if not a:
    print('0')
else:
    c = a // b
    if c:
        if c == -1:
            c = 0
        else:
            ans.append(str(c))
    if b != 1:
        ans.append(f"{a - c * b}/{b}")
    print(*ans)
