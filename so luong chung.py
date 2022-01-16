def common_member(a, b):   
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return len((a_set.intersection(b_set)))
    else:
        return 0
a=input()
b=input()
arr=a.split()
arr2=b.split()
print(common_member(arr,arr2))