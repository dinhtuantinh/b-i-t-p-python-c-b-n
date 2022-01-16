n= int(input())
dict= {}

for i in range(0, n):
  a = input()
  arr=a.split()
  if arr[0] not in dict:
    dict[arr[0]]= int(arr[1])
  else :
    dict[arr[0]] += int(arr[1])

for i in sorted(dict.keys()):
    print(i,dict[i])