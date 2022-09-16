ch=input("enter character")
try:
	int(ch)
	print("{} is a digit".format(ch))
except:
	print("not digit")

