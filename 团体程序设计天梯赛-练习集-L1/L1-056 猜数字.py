n = int(input())

ls, s = [], []
for i in range(n):
    a, b = input().split()
    ls.append((a, int(b)))
    s.append(int(b))

s = int(sum(s) / (n * 2))
l = sorted(ls, key=lambda x: abs(x[1] - s))
print(s, l[0][0])
