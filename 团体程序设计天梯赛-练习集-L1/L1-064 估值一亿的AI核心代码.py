import re

for i in range(int(input())):
    s = input()
    print(f'{s}\nAI:', end=' ')

    s = ' '.join(s.split())

    for j in s:
        if j != 'I':
            s = s.replace(j, j.lower())

    for a, b in [(' \?', '!'), ('\?', '!'), (' \'', '\''),(r'(\bcan you\b)', '_I can'), (r'(\bcould you\b)', '_I could'), (r'(\bI\b)', 'you'), (r'(\bme\b)', 'you'), (r'(\b_I\b)', 'I')]:
        s = re.sub(a, b, s)

    print(s)
