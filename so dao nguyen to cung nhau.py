def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)
t=int(input())
for test in range(t):
    s = str(input())
    res = s[::-1]
    if(USCLN(int(s), int(res))==1):
        print("YES")
    else:
        print("NO")
