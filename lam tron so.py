for _ in [0]*int(input()):
    n = input()
    r = 0
    for i in n[:0:-1]:
        r = 1 if (int(i) + r >= 5) else 0
    print([n[0], str(int(n[0]) + 1)][r] + "0"*(len(n) - 1))
