a = int(input())

for i in range(a):
    s1, s2 = input().split(', ')
    if s1[-3:] == 'ong' == s2[-4:-1]:
        l = s2.split()[:-3] + ['qiao ben zhong.']
        print(s1 + ', ' + ' '.join(l))
    else:
        print('Skipped')
        