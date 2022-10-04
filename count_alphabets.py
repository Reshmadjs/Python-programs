# Remember You are doing it for yourself, To build yourself stronger  


# Write a function that accepts a character as parameter and returns 1 if it is an alphabet, 2 if it
# is a digit and 3 if it is a special symbol. In main, accept characters till the user enters EOF and use
# the function to count the total number of alphabets, digits and special symbols entered.

def count(n):
	if 122>=ord(n)>=97 or 90>=ord(n)>=65:
		return 1
	elif 57>=ord(str(n))>=48:
		return 2
	else:
	 return 3	


n=input("enter char")
if count(n)==1:
	print("alphabet")
elif count(n)==2:
	print("digit")
else:
	print("spcl symbol")

if __name__=="__main__":
	character=digit=spl_symbol=0
	while(True):
		ch=input("enter char")
		if 122>=ord(ch)>=97 or 90>=ord(ch)>=65:
			character+=1
		elif 57>=ord(str(ch))>=48:
			digit+=1
		elif 32<=ord(str(ch))<=47 or 64>=ord(str(ch))>=58 or 123>=ord(str(ch))<=126 or 91<=ord(str(ch))<=96 :
			spl_symbol+=1

		if(ch==' '):
			break

	print("No of alphabets: {} ,No of digit: {} and No of spcl symbol: {}".format(character,digit,spl_symbol))		


