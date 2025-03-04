def matrix_multiply(a, b):
    if len(a[0]) != len(b):
        return False, len(a[0]), len(b)

    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return True, result

a = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
b = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]

c = matrix_multiply(a, b)

if c[0]:
    print(f'{len(c[1])} {len(c[1][0])}')
    for i in c[1]: print(*i)
else:
    print(f"Error: {c[1]} != {c[2]}")
