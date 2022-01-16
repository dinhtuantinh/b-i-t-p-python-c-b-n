n=int(input())
ktr=0
F = []
F.append(1)
F.append(1)
for i in range (2,93):
    F.append(F[i-1] + F[i-2])
for i in range(93):
    if F[i]==n:
        print(i+1)
        ktr=1
if ktr ==0:
    print(-1)