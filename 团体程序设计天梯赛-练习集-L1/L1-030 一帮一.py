t = int(input())

l1, l2 = [], []

for i in range(t):
    a, b = input().split()
    if a == '0':
        l1.append((i, b))
    else:
        l2.append((i, b))

for i in range(t // 2):
    if l1[0] < l2[0]:
        ls = l1.pop(0), l2.pop()
    else:
        ls = l1.pop(), l2.pop(0)
    ls = sorted(ls, key=lambda i: i[0])
    print(ls[0][1], ls[1][1])
    