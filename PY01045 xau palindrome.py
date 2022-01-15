def palindrome(s,n):
    if n<1: return 1
    elif s[0]!=s[n]: return 0
    else: return palindrome(s+1,n-2)
s=str(input())
k=palindrome(s,len(s)-1)
if k==0: print("NO")
else:print("YES")