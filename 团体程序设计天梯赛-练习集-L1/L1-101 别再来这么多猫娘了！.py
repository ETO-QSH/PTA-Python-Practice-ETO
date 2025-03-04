l = int(input())
ls = [input() for i in range(l)]
n = int(input())
s = input()

for i in ls:
    if i in s:
        s = s.replace(i, '明日方舟')
        
if s.count('明日方舟') >= n: print(f"{s.count('明日方舟')}\nHe Xie Ni Quan Jia!")
else: print(s.replace('明日方舟', '<censored>'))
