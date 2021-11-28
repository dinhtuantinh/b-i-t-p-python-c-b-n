s=str(input())
while len(s)>1:
    right=len(s)
    left=len(s)//2
    sum1="";sum2=""
    tmp=0
    for i in range(0,left):
        sum1+=s[i]
    for i in range(left,right):
        sum2+=s[i]
    tmp=int(sum1)+int(sum2)
    s=str(tmp)
    print(s)