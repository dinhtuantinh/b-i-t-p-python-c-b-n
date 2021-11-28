def tongchuso():
    s=list(input())
    s.sort()
    res=""
    tong=int(0)
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            tong+=int(s[i])
        else: res+=s[i]
    res+=str(tong)
    print(res)
t=int(input())
for i in range(t): tongchuso()
