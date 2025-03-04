a = list(map(int, input().split()))

while True:
    t = eval(input())
    if t in range(0, 24):
        print(a[t], 'Yes' if a[t] > 50 else 'No')
    else:
        break
        