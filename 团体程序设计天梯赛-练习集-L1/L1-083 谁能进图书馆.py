a, b, c, d = map(int, input().split())

q, p = c, d
c, d = sorted((c, d))
r = 2 if c != q else 1

if c >= a:
    print(f'{q}-Y {p}-Y')
    print('huan ying ru guan')
elif d <= a:
    print(f'{q}-N {p}-N')
    print('zhang da zai lai ba')
elif c <= a and b > d >= a:
    if r == 2:
        print(f'{q}-Y {p}-N')
    else:
        print(f'{q}-N {p}-Y')
    print(f'{1 if r == 2 else 2}: huan ying ru guan', end='')
elif c <= a and d >= a:
    print(f'{q}-Y {p}-Y')
    print(f'qing {1 if r == 2 else 2} zhao gu hao {r}')
