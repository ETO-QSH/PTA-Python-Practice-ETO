N = int(input())

dic = {}
for i in range(N):
    temp = input().split()[1:]
    for j in temp:
        if j in dic:
            dic[j].append(i)
        else:
            dic[j] = [i]

ls = sorted(dic, key=lambda x: (len(dic[x]), int(x)))
print(ls[-1], len(dic[ls[-1]]))
