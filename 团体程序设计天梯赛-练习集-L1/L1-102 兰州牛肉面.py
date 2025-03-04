n = int(input())
lst = input().split()
D = [0] * n

while True:
    a, b = map(int, input().split())
    if a == 0: break
    else: D[a-1] += b

print('\n'.join(map(str, D)))
print(f'{sum([float(lst[i]) * D[i] for i in range(n)]):.2f}')
