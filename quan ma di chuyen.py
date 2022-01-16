import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (abs(a-c)==1 and abs(b-d)==2) or (abs(b-d)==1 and abs(a-c)==2):
    print("YES")
else:
    print("NO")