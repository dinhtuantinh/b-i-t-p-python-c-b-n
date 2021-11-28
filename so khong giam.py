import re
t=int(input())
for i in range(t):
    s=str(input())
    check=0
    for j in range (len(s)-1):
        if (s[j]>s[j+1]):
            check=1
            break;
    if(check==0):
        print("YES")
    else:
        print("NO")
