n, m = map(int, input().split())

if n in [0, 1]:
    if m == 1: print("-")
    else: print("biii") if n == 0 else print("dudu")
else: print("-")

if n in [0, 2]: print("stop")
else: print("move")
