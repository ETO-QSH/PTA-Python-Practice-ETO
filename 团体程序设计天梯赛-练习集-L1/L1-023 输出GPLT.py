a = input()

G = a.count('G')+a.count('g')
P = a.count('P')+a.count('p')
L = a.count('L')+a.count('l')
T = a.count('T')+a.count('t')

while sum([G, P, T, L]) > 0:
    if G > 0:
        G -= 1
        print('G', end='')
    if P > 0:
        P -= 1
        print('P', end='')
    if L > 0:
        L -= 1
        print('L', end='')
    if T > 0:
        T -= 1
        print('T', end='')
print()
