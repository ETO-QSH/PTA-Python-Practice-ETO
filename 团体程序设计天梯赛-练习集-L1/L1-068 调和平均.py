N = int(input())
m = [eval(i) for i in input().split()]
s = sum(1 / i for i in m)
print("%.2f" % (1 / (s / N)))
