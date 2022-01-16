n = int(input())
dict = {}
for i in range(n):
    arr = list(input().split())
    dict[arr[0]] = arr[1:len(arr)]
m = int(input())
for t in range(m):
    a = list(input().split())
    if 'W' in dict[a[1]] and a[0] == 'write':
        print('OK')
    elif 'R' in dict[a[1]] and a[0] == 'read':
        print('OK')
    elif 'X' in dict[a[1]] and a[0] == 'execute':
        print('OK')
    else:
        print('Access denied')