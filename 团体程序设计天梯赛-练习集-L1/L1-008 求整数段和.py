a, b = map(int, input().split())
lst = list(range(a, b+1))

for i in range(0, len(lst)+1, 5):
    if i+5 == len(lst):
        print(''.join([f'{i:>5}' for i in lst[i:i+5]]), end='')
    else:
        print(''.join([f'{i:>5}' for i in lst[i:i+5]]))

print(f'Sum = {sum(lst)}')
