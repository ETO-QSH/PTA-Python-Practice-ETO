dic = [0]*10

for i in input():
    dic[int(i)] += 1

lst = [[i, j] for i, j in enumerate(dic) if j != 0]

ls = sorted(lst, key=lambda x: int(x[0]))

for i in ls:
    print(f"{i[0]}:{i[1]}")
    