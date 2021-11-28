array = [1,2,3,4,5,2,4,34,5,24,2]
array2 = array[2:5]
print("mang array 1 gom cac phan tu la:\n")
for i in array:
    print(i)
print("\nin doan [4,10] trong mang array\n")
for i in array[4:10]:
    print(i)
print("\nin tu dau mang den phan tu thu 5 cua array:\n")
for i in array[:5]:
    print(i)
print("\nin tu phan tu thu 5 den cuoi mang array:\n")
for i in array[5:]:
    print(i)
print("\nin mang array 2 copy doan phan tu tu 2 den 5 cua mang array:\n")
for i in array2:
    print(i)
