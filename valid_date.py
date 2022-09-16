def check_if_present_in_list(list, element):
	return (element in list)

day,month,year=[int(x) for x in input("enter day:month:year").split()]
date_valid = False

thirty_1st_days_month = check_if_present_in_list([1,3,5,7,8,10,12], month)
thirty_days_month = check_if_present_in_list([4,6,9,11], month)
is_leap_year = (year%4==0 and year%100!=0 or year%400==0)

if 1<=month<=12:

	if month==2 and ((is_leap_year and 1<=day<=29) or (1<=day<=28)):
		date_valid = True
	elif ((thirty_days_month) and 1<=day<=30) or ((thirty_1st_days_month) and 1<=day<=31):
		date_valid = True

if date_valid:
	print("{}:{}:{} is valid date".format(day,month,year))	
else:
	print("invalid date")										
