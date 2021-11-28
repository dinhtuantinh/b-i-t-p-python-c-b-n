def main():
	n = input()
	cnt = 0
	while len(n) > 1:
		digits = [ord(i) - ord('0') for i in n]
		n = str(sum(digits))
		cnt += 1
	print(cnt)
	
main()
