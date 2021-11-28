s1 = str(input())
s2 = str(input())
k = int(input())
k=k-1
s = s1[:k]+s2+s1[k:]
print(s)
