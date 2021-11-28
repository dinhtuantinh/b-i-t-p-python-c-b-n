def main():
    for _ in range(int(input())):
        s = input()
        s1 = Rotate(s[:len(s)//2])
        s2 = Rotate(s[len(s)//2:])
        ans = ""
        ans = [chr((ord(s1[i])-65+ord(s2[i])-65) % 26+65)
               for i in range(len(s1))]
        for x in ans:
            print(x, end="")
        print()
def Rotate(s):
    sum = 0
    ans = ""
    for x in s:
        sum += ord(x)-65
    sum %= 26
    ans = [chr((sum+ord(x)-65) % 26+65) for x in s]
    return ans
main()
