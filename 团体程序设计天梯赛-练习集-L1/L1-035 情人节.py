lst = []
while True:
    try: lst.append(input())
    except: break
    
lst = lst[:-1]
if len(lst) > 13:
    print(f'{lst[1]} and {lst[13]} are inviting you to dinner...')
elif len(lst) > 1:
    print(f'{lst[1]} is the only one for you...')
else:
    print('Momo... No one is for you ...')
