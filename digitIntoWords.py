n=int(input("enter digit"))
lst=['zero','one','two','three','four','five','six','seven','eight','nine']
def fun(n):
	if n<=0:
		return ""
	# rem=(n%10)
	word=lst[n%10]
	# ans= fun(int(n/10),lst)+" "+lst[rem]+" "
	ans= fun(int(n/10))+" "+word+" "
	return ans

print(fun(n))	