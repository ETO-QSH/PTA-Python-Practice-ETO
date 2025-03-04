s = input().split()
r = float(s[0])
if s[1] == '0': r *= 2.455
else: r *= 1.26
print('%.2f' % (r),end=' ')
if r < float(s[2]): print('^_^')
else: print('T_T')
