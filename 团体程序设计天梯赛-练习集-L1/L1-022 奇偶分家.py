n = int(input())
lst = list(map(int, input().split()))

o = sum([1 for i in lst if i%2==0])
print(n - o, o)
