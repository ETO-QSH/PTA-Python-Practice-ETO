a, b = map(int, input().split())

def nm(s):
    k = 0
    while len(s) > 1:
        y = 1
        for j in [int(i) for i in s]:
            y *= j
        s, k = str(y), k + 1
    return k

ll = [nm(str(s)) for s in range(a, b+1)]

print(max(ll))
print(*[i for i in range(a, b+1) if ll[i-a] == max(ll)])
