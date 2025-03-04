for i in range(int(input())):
    res = []
    books = [None] * 1001
    while True:
        name, cmd, time = input().split()
        if name == '0':
            print(len(res), round(sum(res) / len(res)) if res else 0)
            break
        if cmd == 'S':
            books[int(name)] = time.split(':')
        elif cmd == 'E' and books[int(name)]:
            a, b = books[int(name)]
            c, d = time.split(':')
            books[int(name)] = None
            res.append((int(c) - int(a)) * 60 + (int(d) - int(b)))
