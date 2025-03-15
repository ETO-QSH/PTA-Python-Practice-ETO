numL = [list(map(int, input().split())) for k in range(int(input()))]
i = int(input())
lst = list(map(int, input().split()))
[print(j[0], j[2]) for i in lst for j in numL if j[1] == i]
