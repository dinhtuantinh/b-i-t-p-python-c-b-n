s=str(input())
if len(s)%2==0:
    for i in range((len(s)//2),len(s)):
        print(s[i],end='')
    for i in range(len(s)//2):
        print(s[i],end='')
else:
    for i in range((len(s)//2)+1,len(s)):
        print(s[i],end='')
    for i in range(len(s)//2+1):
        print(s[i],end='')
print()