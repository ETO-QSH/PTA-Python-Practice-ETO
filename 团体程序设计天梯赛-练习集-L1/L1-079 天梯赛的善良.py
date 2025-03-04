a = int(input())
ls = list(map(int, input().split()))

MIN, MAX = min(ls), max(ls)

print(MIN, ls.count(MIN))
print(MAX, ls.count(MAX))
