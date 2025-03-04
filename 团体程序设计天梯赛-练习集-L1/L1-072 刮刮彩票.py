dict1 = {'6': 10000, '7': 36, '8': 720, '9': 360, '10': 80, '11': 252, '12': 108, '13': 72, '14': 54, '15': 180, '16': 72, '17': 180, '18': 119, '19': 36, '20': 306, '21': 1080, '22': 144, '23': 1800, '24': 3600}
l, d = [], list(map(str, range(1, 10)))

for i in range(3):
    data = input().split()
    [d.remove(j) for j in data if j in d]
    l.append(data)
    
for i in range(3):
    for j in range(3):
        if l[i][j] == '0':
            l[i][j] = d[0]
 
a1, a2, a3, a4 = input().split(), input().split(), input().split(), int(input())
 
print(l[int(a1[0]) - 1][int(a1[1]) - 1])
print(l[int(a2[0]) - 1][int(a2[1]) - 1])
print(l[int(a3[0]) - 1][int(a3[1]) - 1])

if a4 == 1: sum1 = sum(int(i) for i in l[0])
elif a4 == 2: sum1 = sum(int(i) for i in l[1])
elif a4 == 3: sum1 = sum(int(i) for i in l[2])
elif a4 == 4: sum1 = sum(int(l[i][0]) for i in range(3))
elif a4 == 5: sum1 = sum(int(l[i][1]) for i in range(3))
elif a4 == 6: sum1 = sum(int(l[i][2]) for i in range(3))
elif a4 == 7: sum1 = int(l[0][0]) + int(l[1][1]) + int(l[2][2])
else: sum1 = int(l[0][2]) + int(l[1][1]) + int(l[2][0])

print(dict1[str(sum1)])
