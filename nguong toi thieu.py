def main():
	s=input()
	check=dict()
	ans=list()
	k=int(input())
	n=0
	if len(s)%2==0:
		n=len(s)
	else :
		n=len(s)-1
	for i in range(0,n,2):
		tmp=s[i]+s[i+1]
		if not(tmp in check):
			check[tmp]=0
			ans.append(tmp)
		check[tmp]+=1
	ans.sort()
	check_1=False
	for i in ans:
		if check[i]>=k:
			print(str(i)+" "+str(check[i]))
			check_1=True
	if check_1==False: 
	    print("NOT FOUND")
main()
