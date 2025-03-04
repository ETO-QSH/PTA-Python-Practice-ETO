a = list(map(int, input().split()))
s, f = 0, 0
b = sorted(a[i] for i in range(4))

for i in range(len(b)):
    if b[(len(b) - 1)] - a[i] > a[len(a) - 1] or a[i] < a[len(a) - 2]:
        f, s = i + 1, s + 1
        
if s == 0: print('Normal')
elif s == 1: print("Warning: please check #%d!" % f)
else: print("Warning: please check all the tires!")
