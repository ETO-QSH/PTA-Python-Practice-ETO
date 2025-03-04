n, m = map(int, input().split())
s = sum(map(int, input().split())) - n * (m - 1)
print(0 if s < 0 else s)
