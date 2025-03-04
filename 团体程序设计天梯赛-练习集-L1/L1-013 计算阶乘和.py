N = int(input())

s, j = 0, 1
for n in range(1, N+1):
    j *= n
    s += j
print(s)
