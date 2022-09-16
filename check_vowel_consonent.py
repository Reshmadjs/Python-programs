ch=input("give character")
# try:
	# int(ch)
if ch == 'a' or  ch=='e' or ch=='i' or ch=='o' or ch=='u':
	print("vowel")
	
else:
	try:
		int(ch)
		print("Digit")

	except:
		print("consonent")



	
