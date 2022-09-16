books,no_of_days=[int(x) for x in input("enter how many books and number of dayss").split()]
if no_of_days<=5:
	fine=50*books
	print("fine of {} books is {} ".format(books,fine))
elif 10>=no_of_days>=6:
	fine=books*70
	print("fine of {} books is {} ".format(books,fine))
elif no_of_days>10:
	fine=books*100
	print("fine of {} books is {} ".format(books,fine))	