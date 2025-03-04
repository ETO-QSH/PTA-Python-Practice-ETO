N = int(input())
ls = [[i, int(j)] for i, j in enumerate(input().split())]
lst = [[] for _ in range(N)]

sep, last = 1, -1
while ls:
    if len(ls) == 1:
        j, k = ls.pop()
        if last != -1 and j == last: sep += 1
        lst[j].append(list(range(sep, sep + 20, 2)))
        if k != 1: ls, sep, last = [[j, k - 1]], sep + 19, j 
    else:
        MIN = min(ls, key=lambda x: x[1])[1]
        for i in range(MIN):
            for l, (j, k) in enumerate(ls):
                lst[j].append(list(range(sep + l, sep + l + len(ls) * 10, len(ls))))
            sep += len(ls) * 10
        last, ls = ls[-1][0], [[j, k-MIN] for j, k in ls if k != MIN]

for i, j in enumerate(lst, 1):
    print(f"#{i}")
    for k in j:
        print(*k)
