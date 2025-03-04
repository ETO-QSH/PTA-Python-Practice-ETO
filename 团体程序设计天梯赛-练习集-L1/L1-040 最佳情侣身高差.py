n = int(input())

for i in range(n):
    gender, height = input().split()
    if gender == 'F':
        print(f'{float(height)*1.09:.2f}')
    elif gender == 'M':
        print(f'{float(height)/1.09:.2f}')
        