t=int(input())
for test in range(t):
    s=str(input())
    check=0
    for i in range(len(s)-2):
        if s[i]!=s[i+2]:
            check=1
            break
    if check==0:print("YES")
    else: print("NO")