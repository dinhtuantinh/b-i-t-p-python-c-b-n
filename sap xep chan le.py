n=int(input())
a=[]
while len(a)<n:
    a.extend(list(map(int, input().strip().split())))
chan=[]
le=[]
for i in a:
    if i%2==1: le.append(i)
    else: chan.append(i)
chan.sort()
le.sort(reverse=True)
mark1=0
mark2=0
for i in a:
    if i%2==1:
        print(le[mark1],end=' ')
        mark1+=1
    else:
        print(chan[mark2],end=' ')
        mark2+=1
