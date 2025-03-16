n, m = map(int, input().split())

if n in [0, 1]:
    if m == 1: print("-")
    else: print("biii" if n == 0 else "dudu")
else: print("-")

print("stop" if n in [0, 2] else "move")
