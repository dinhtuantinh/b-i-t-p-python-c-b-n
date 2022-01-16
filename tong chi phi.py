a=int(input())
b=int(input())
n=int(input())
do=a*n
xu=b*n
s=0
if xu>=100:
    s=xu%100
    xu=xu//100
    do+=xu
    print(do,s)
else:
    print(do,xu)