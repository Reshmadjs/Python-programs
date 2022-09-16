string=input("enter string")
count1=0
count2=0
for i in string:
	if 65<=ord(i)<=90 or 97<=ord(i)<=122:
		count1+=1
		print("char value: {}".format(i))
	elif 48<=ord(i)<=57:
		count2+=1
		print("digit : {}".format(i))
	else:
		print("values are other than alphabet and digit")


print("number of alphabets are %d and number of digits are %d" % (count1,count2))

