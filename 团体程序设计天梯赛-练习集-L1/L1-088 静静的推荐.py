N, K, S = map(int, input().split())
r, t = 0, {}
for n in range(N):
    a, b = map(int, input().split())
    if a > 174:
        if b >= S: r += 1
        elif a in t and t[a] < K: t[a] += 1
        else: t[a] = 1

print(sum(t.values()) + r)
