for i in range(int(input())):
    q, w, e = input().split()
    if (not 15 <= int(w) <= 20) or (not 50 <= int(e) <= 70):
        print(q)
