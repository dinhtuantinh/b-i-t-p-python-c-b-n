import re
s=input()
a=0

for i in range(0, s.__len__()):
        if(s[i].islower()):
           a+=1
if(a>= s.__len__()/2):
    s=s.lower()
else:
    s=s.upper()
print(s)
