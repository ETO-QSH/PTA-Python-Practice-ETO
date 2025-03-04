#import re
#i = int(input())
#[print('No') if re.search(r'^1?$|^(11+?)\1+$', '1'*int(input())) else print('Yes') for m in range(i)]

def is_p(n):
    if n < 2:
        return "No"
    else:
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                return "No"
        return "Yes"
                
k = int(input())
for m in range(k):
    print(is_p(int(input())))
