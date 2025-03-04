n = int(input())
factors = [i for i in range(2, int(n ** 0.5 + 2)) if n % i == 0]

if factors:
    long = pos = 0
    for i in range(len(factors)):
        cp, cl = factors[i], 1
        for j in range(i, len(factors) - 1):
            if factors[j + 1] - factors[j] == 1 and n % (cp * factors[j + 1]) == 0:
                cp, cl = cp * factors[j + 1], cl + 1
            else:
                break
        if cl > long or (cl == long and factors[i] < factors[pos]):
            long, pos = cl, i
    print(f"{long}\n{'*'.join(map(str, factors[pos: pos + long]))}" if long else f"1\n{factors[0]}")
else:
    print(f"1\n{n}")
