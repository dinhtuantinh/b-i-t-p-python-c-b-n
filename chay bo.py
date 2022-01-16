x=float(input())
y=float(input())
if x>=y:
    print(1)
else:
    n=1
    while(True):
        x=x+x*(float)(0.1)
        n+=1
        if x>=y:
            break
        
    print(n)