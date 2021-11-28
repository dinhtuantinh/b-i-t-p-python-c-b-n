#import re
T=int(input())
for t in range(T):
    s=str(input())
    dem=1
    s=s+' '
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            dem+=1
        else:
           print(dem,end='')
           dem=1
           print(s[i],end='')
    print()
