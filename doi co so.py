def convert(n,b):
    res=""
    temp=n
    while temp>0:
        du=temp%b
        if du>=10: res+=str(chr(du+55))
        else:res+=str(du)
        temp=int(temp/b)
    print("".join(reversed(res)))
def initwsolve():
    n,b = map(int,input().split())
    convert(n,b)

t=int(input())
for i in range(t): initwsolve()
