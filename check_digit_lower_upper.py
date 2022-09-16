ch=input("enter number")
if chr(58)>=ch>=chr(48):
	print("{} is a digit".format(ch))
elif chr(122)>=ch>=chr(97):
	print("{} is a lower case character".format(ch))
elif chr(90)>=ch>=chr(65):
	print("{} is a upper case character".format(ch))


# chr() for getting values like alphabates, digits from ascii numbers Ex.chr(65)='A'
# ord() for getting ascii numbers Ex. ord(c)=112

