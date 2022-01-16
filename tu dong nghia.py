n = int(input())
dic = {}
s = list(input().split())
for i in range (n):
    dic[s[0]] = s[1]
    if i < n-1:
        s = list(input().split())
word = input()
for k, v in dic.items():
    if k == word:
        print(v)
    if v == word:
        print(k)