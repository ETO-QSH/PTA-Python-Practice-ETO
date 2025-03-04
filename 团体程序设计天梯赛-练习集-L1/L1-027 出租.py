n = input()
a = sorted(list(set([i for i in n])))[::-1]

print(f'int[] arr = new int[]{{{",".join(a)}}};')
print(f'int[] index = new int[]{{{",".join([str("".join(a).find(i)) for i in n])}}};')
