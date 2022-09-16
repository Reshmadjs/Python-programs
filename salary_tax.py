salary=int(input("enter ur basic salary"))
if salary<150000:
	print("tax is zero")
elif 300000>salary>=150000:
	tax=(salary/100)*20
	print("income tax on {} is {}" .format(salary,tax))
else:
	tax=(salary/100)*30
	print("income tax on {} is {}" .format(salary,tax))


