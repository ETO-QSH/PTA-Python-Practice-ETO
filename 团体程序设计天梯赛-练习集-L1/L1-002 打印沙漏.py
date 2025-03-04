s, c = input().split()
m, n = int(s), 1

while ((n+3)**2)/2-1 <= m:
    n += 2

l = list(range(1, n+1, 2))

for i in l[::-1]+l[1:]:
    print(f"{f'{c}'*i: ^{n}}".rstrip())

print(int(m-(((n+1)**2)/2-1)))
