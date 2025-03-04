a, b, c = map(int, input().split())

lst = [a, b]
index = 0

while len(lst) < c:
    index, lst = index + 1, lst + [int(i) for i in str(lst[index] * lst[index+1])]
print(*lst[:c])
