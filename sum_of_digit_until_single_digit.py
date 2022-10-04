# Write a recursive function to calculate the sum of digits of a number till you get a single digit
# number. Example: 961 -> 16 -> 7. (Note: Do not use a loop)

n=int(input("enter number"))
sum=0
def digit(n):
	global sum
	if n==0:
		return 0
	else:	
		rem=n%10
		sum=sum+rem
		digit(int(n/10))
		# singl_digit(sum)
		return sum



	

# def singl_digit(two_digit):
	
# 	final=digit(two_digit)
		
# 	return final	


# two_digit=digit(n)
# print(two_digit)
# print(singl_digit(two_digit))
# print(value)	

# if digit(n)>9:
# 	digit(n)
# 	print(sum)

# else:
# 	print(digit(n))	
