t=int(input())
for test in range(t):
    s=str(input())
    tich=1
    for i in range(len(s)):
        if int(s[i])==0:
            continue
        else:
            tich=tich*int(s[i])
    print(tich)
