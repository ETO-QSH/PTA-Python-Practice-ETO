a, b = input().split()
lst = []

for i in range(int(b)):
    lst.append(input().replace("@", a))

if lst == lst[::-1]:
    print('bu yong dao le')
    for i in lst:
        print(i)
else:
    for i in lst[::-1]:
        print(i[::-1])
