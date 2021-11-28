def main():
	n=int(input())
	array = [int(x) for x in input().split()]
	for i in range(1,300000):
		if not(i in array):
			print(i)
			break

main()
