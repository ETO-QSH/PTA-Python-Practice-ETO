i, x = 1, int(input())
while True:
    if int('1' * i) % x == 0:
        print(int('1' * i) // x, i)
        break
    i += 1
