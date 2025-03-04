str = input()
for i in range(int(input())):
    a, b, c, d = input().split()
    str1 = str[int(a) - 1:int(b)]
    str = str[:int(a) - 1] + str[int(b):]
    if c + d not in str: str += str1
    else: str = str.replace(c + d, c + str1 + d, 1)
print(str)
