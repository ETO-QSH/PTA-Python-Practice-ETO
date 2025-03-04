friends_ID = set()
handsome_ID = []
N = int(input())

for i in range(N):
    K = input().split()
    if K[0] != '1':
        friends_ID.update(K)

M = int(input())
check_ID = input().split()

for i in check_ID:
    if i not in friends_ID:
        handsome_ID.append(i)
        friends_ID.add(i)

if handsome_ID:
    print(*handsome_ID)
else:
    print('No one is handsome')
