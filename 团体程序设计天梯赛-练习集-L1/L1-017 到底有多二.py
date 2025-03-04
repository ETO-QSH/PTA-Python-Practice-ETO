a = int(input())

fu = True if a < 0 else False
er = True if a % 2 == 0 else False

num = (str(a).count('2')/len(str(abs(a))))*((3 if er else 1.5) if fu else 1)
num = (str(a).count('2')/len(str(abs(a))))*(1.5 if fu else 1)*(2 if er else 1)
print(f'{num*100:.2f}%')
