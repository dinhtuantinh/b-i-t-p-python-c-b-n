import re
t=int(input())
for i in range(t):
    s = str(input())
    for j in range (len(s)):
        if(s[j]>'0' and s[j]<='9'):
            dem=int(s[j])
            for k in range(dem):
                print(s[j-1],end="")
        else:
            continue
    print()
