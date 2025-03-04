def goto(num):
    return ''.join(str(max(int(num[i]), int(num[i - 1]))) for i in range(1, len(num)) if int(num[i]) % 2 == int(num[i - 1]) % 2)

s1, s2 = goto(input()), goto(input())
print(s1) if s1 == s2 else print(f'{s1}\n{s2}')
