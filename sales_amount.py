qty1,qty2,qty3=[int(x) for x in input("enter quantity for qty1,qty2 and qty3").split()]
rate1,rate2,rate3=[float(x) for x in input("enter rate of one qty1,one qty2,one qty3").split()]
total_amount=(qty1*rate1)+(qty2*rate2)+(qty3*rate3)
print("total amount is ",total_amount)
if total_amount>7000:
	print("discount is 20%")
	total_discount=(total_amount/100)*20
	print("total  discount of 20% is {}".format(total_discount))
elif 4000<total_amount<=7000:
	print("discount is 15%")
	total_amount=(total_amount/100)*15
	print("total  discount of 15% is {}".format(total_discount))	
elif 1000<total_amount<=4000:
	print("discount is 8%")
	total_amount=(total_amount/100)*8
	print("total  discount of 8% is {}".format(total_discount))	
else:
	 print("no discount")			