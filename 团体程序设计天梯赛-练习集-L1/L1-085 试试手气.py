l = list(map(int, input().split()))
t, a = int(input()), locals()

for i in range(6):
    a[f"a{i}"] = [6, 5, 4, 3, 2, 1]

[j.remove(l[i]) for i, j in enumerate([a[f"a{i}"] for i in range(6)])]
print(*[i[t - 1] for i in [a[f"a{i}"] for i in range(6)]])
