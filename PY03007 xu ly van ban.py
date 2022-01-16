#s = re.sub(r"\s+", " ", s, flags=re.UNICODE)
import re
s = ""
while True:
    ans = input()
    s += ans+" "
    if ans[-1] == '.':
        break
a = re.split("\?|\.|\!", s)
for x in a:
    i = x.title().strip()
    ans = re.split("\\s+", i)
    for i in range(len(ans)):
        print(ans[i] if i == 0 else ans[i].lower(), end=" ")
    print()