n, s = input().split()
t = input()

if len(t) > int(n):
    print(t[len(t)-int(n):])
else:
    print(f'{s}'*(int(n)-len(t))+t)
