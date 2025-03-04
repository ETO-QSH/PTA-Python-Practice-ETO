x, a, b = 1, [], []

while True:
    x = input()
    if x == '.':
        break
    a.append(x)

for i, j in enumerate(a, 1):
    if "chi1 huo3 guo1" in j:
        b.append(i)

print(len(a))
print('-_-#') if len(b) == 0 else print(b[0], len(b))
