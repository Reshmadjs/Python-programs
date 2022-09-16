# digit=int(input("enter digit"))
list=["zero","one","two","three","four","five","six","seven","eight","nine"]

def digit_to_num(n):
	if n==0:
		return ""
	# mod of single digit is that digit itself	
	word=list[n%10]        
	final=digit_to_num(int(n/10))+" "+word
	return final
	
n=int(input("enter number"))
print(digit_to_num(n))	


# recursion performs operations from last one to first 