a = int(input())

for i in range(a):
    h, w = map(int, input().split())
    w = w / 2
    standard_weight = (h - 100) * 0.9
    error = abs(w - standard_weight)
    standard_weight_10_percent = standard_weight * 0.1
    if error < standard_weight_10_percent:
        print('You are wan mei!')
    elif w > standard_weight:
        print('You are tai pang le!')
    else:
        print('You are tai shou le!')
        