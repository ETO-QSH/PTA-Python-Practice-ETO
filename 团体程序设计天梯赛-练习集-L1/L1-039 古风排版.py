N = int(input())
text = input()

chunks = [f'{text[i: i + N]:<{N}}' for i in range(0, len(text), N)]
[print(''.join(item)[::-1]) for item in zip(*chunks)]
