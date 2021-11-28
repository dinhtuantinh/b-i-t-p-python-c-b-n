def isThuanNghich(n):
    str1 = str(n)     # ep kieu so n thanh chuoi
    str2 = str1[::-1] # dao nguoc chuoi str1
    if (str1 == str2):
        return True
    else:
        return False
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
tn=0
for i in range(n):
    for j in range(m):
        if isThuanNghich(a[i][j])==1 and a[i][j]>10 and a[i][j]>tn:
            tn=a[i][j];
if tn==0:
    print("NOT FOUND")
else:
    print(tn)
    for i in range(n):
        for j in range(m):
            if a[i][j]==tn:
                print("Vi tri [",end='')
                print(i,end=']')
                print('[',end='')
                print(j,end=']')
                print()
