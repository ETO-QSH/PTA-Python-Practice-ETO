n, m = map(int, input().split())

def base26(n):
    if n < 26:
        return chr(n + 96)
    else:
        return base26(n // 26) + base26(n % 26)

S = [chr(ord('z')-ord(i)+ord('a')-1) for i in base26(m-1)]

print('z'*(n-len(S))+''.join(S))
