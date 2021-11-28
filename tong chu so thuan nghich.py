def isThuanNghich(n):
    if n<11:
        return False
    str1 = str(n)     # ep kieu so n thanh chuoi
    str2 = str1[::-1] # dao nguoc chuoi str1
    if (str1 == str2):
        return True
    else:
        return False
t=int(input())
for test in range(t):
    x=str(input())
    s=0
    for i in range(len(x)):
        s+=int(x[i])
    check1=0
    #check2=0
    if isThuanNghich(s): check1=1
    '''
    s1=str(s)
    for i in range(len(s1)-1):
        if s1[i]!=s1[i+1]:
            check2=1
            break
    '''
    if check1==1:
        print("YES")
    else: print("NO")
