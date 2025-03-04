a, b, c = map(int, input().split())

ls = []
for i in range(1, c):
    a_d, a_m = divmod(a, i)
    if a_m == 0 and c != a_d:
        b_d, b_m = divmod(b, c - a_d)
        if b_m == 0 and a != a_d:
            ls.append((a_d, c - a_d))

print(*sorted(ls, key=lambda x: abs(a // x[0] - b // x[1]))[0]) if ls else print("No Solution")
