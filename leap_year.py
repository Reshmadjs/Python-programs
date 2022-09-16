# year=int(input("enter year"))
# if year%4==0:
# 	print("{} is leap year".format(year))
# else:
# 	print("NOT")



for i in range(1800,2023):
	if i%4==0 and i%100!=0 and i%400:
		print (i)
