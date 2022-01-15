t=int(input())
for test in range(t):
    s=str(input())
    if(len(s)<3):print("NO")
    else:
        check=1
        for i in range(len(s)):
            if s[i]=='0' or s[i]=='1' or s[i]=='2': continue
            else:
                check=0
                break
        if check==1:print("YES")
        else:print("NO")