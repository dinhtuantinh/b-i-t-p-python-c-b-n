import math
t = int(input())
for test in range (t):
    s1 = str(input())
    s2 = s1[::-1]
    check=1
    for i in range(1,len(s1)):
        a=abs(ord(s1[i])-ord(s1[i-1]))
        b=abs(ord(s2[i])-ord(s2[i-1]))
        if a!=b:
            check=0
            break
    if check==1:
        print("YES")
    else:
        print("NO")
