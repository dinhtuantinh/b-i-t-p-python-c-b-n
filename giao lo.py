def common_member(a, b):   
    lst3 = [value for value in a if value in b]
    return lst3
a=input()
b=input()
a=a.split()
b=b.split()
arr,arr2=[],[]
for i in a:
    arr.append(int(i))
for i in b:
    arr2.append(int(i))
arr.sort()
arr2.sort()
x=common_member(arr,arr2)
for i in x:
    print(i,end=' ')