def isThuanNghich(n):
    str1 = str(n)     # ep kieu so n thanh chuoi
    str2 = str1[::-1] # dao nguoc chuoi str1
    if (str1 == str2):
        return True
    else:
        return False
def isChan(n):
    s = str(n)
    for i in range(len(s)):
        if(int(s[i])%2!=0):
            return False
    return True
def isSoCS(n):
    s = str(n)
    dem=0
    for i in range(len(s)):
        dem+=1
    if dem%2==0: return True
    else: return False
t=int(input())
for test in range(t):
    n=int(input())
    for i in range(n):
        if isThuanNghich(i) and isChan(i) and isSoCS(i):
            print(i,end=" ")
    print()
        
