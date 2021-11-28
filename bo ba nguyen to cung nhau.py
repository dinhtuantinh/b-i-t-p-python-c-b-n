def USCLN(a, b):
    if b == 0:
        return a
    else:
        return USCLN(b, a % b)
l,r = [int(i) for i in input().split()]
x=(l+r)//2
for i in range(l,x+1,1):
    for j in range(i+1,r,1):
        if USCLN(i,j)==1:
            for k in range(j+1,r+1,1):
                if USCLN(j,k)==1 and USCLN(i,k)==1:
                    print("(",end='')
                    print(i,end='')
                    print(",",j,end='')
                    print(",",k,end='')
                    print(")")
