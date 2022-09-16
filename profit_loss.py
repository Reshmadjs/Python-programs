cp,sp=[int(x) for x in input("enter cost price and selling price").split()]
price=cp-sp
if cp>sp:
	print("seller has made profit of {}".format(price))
else:
	print("seller has made loss of {}".format(price))		