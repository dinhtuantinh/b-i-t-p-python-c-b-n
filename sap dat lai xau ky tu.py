def initwsolve(i):
    s1=list(input()); s2=list(input())
    print("Test ",end='')
    print(i+1,end='')
    s1.sort();s2.sort()
    x1=len(s1);x2=len(s2)
    if x1!=x2: print(": NO")
    else:
        res=": YES"
        for i in range(x1):
            if s1[i]!=s2[i]:
                res=": NO"
                break
        print(res)
for i in range(int(input())):
    initwsolve(i)
