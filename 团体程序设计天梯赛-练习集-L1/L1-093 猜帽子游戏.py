n = int(input())
lst = input().split()
m = int(input())

for _ in range(m):
    ls = input().split()
    print('Da Jiang!!!') if sum([1 if lst[i] == ls[i] else -1000 for i in range(n) if ls[i] != '0']) > 0 else print('Ai Ya')
