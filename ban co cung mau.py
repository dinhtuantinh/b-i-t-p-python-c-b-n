def kt(i,j):
    if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
        return True
    return False
i = int(input())
j = int(input())
x = int(input())
y = int(input())
if (kt(i,j)==True and kt(x,y)==True) or (kt(i,j)==False and kt(x,y)==False):
    print("YES")
else:
    print("NO")