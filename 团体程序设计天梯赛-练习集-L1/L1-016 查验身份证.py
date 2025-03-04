lst = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
M, flag = '10X98765432', 0

l = int(input())

for k in range(l):
    a = input()
    if a[:-1].isdigit():
        s = sum(int(a[i]) * lst[i] for i in range(len(a) - 1))
        if str(M[s % 11]) != a[-1]:
            print(a)
            flag = 1
    else:
        print(a)
        flag = 1

if flag == 0:
    print('All passed')
