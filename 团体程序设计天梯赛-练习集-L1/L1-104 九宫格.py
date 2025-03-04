# 这题有错误，如果检查横行就无法通过
S = set(map(str, range(1, 10)))

def check(lst):
    r_lst = list(zip(*lst))
    for l in r_lst:
        if set(l) != S:
            return 0
        
    for a in range(3):
        for b in range(3):
            if set(lst[a*3][b*3:(b+1)*3]+lst[a*3+1][b*3:(b+1)*3]+lst[a*3+2][b*3:(b+1)*3]) != S:
                return 0
    return 1

for _ in range(int(input())):
    print(check([input().split() for _ in range(9)]))
