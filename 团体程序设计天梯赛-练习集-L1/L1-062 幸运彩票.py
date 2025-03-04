a = int(input())

for i in range(a):
    s = [int(i) for i in input()]
    if sum(s[:3]) == sum(s[3:]):
        print('You are lucky!')
    else:
        print('Wish you good luck.')
        