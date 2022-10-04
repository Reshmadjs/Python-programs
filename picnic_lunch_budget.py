# Write a program to calculate the total price for a picnic lunch that a user is purchasing for her
# group of friends. She is first asked to enter a budget for the lunch. She has the option of buying
# apples, cake, and bread. Set the price per kg of apples, price per cake, and price per loaf of bread
# in constant variables. Use a menu to ask the user what item and how much of each item she
# would like to purchase. Keep calculating the total of the items purchased. After purchase of an
# item, display the remaining amount. Exit the menu if the total has exceeded the budget. In
# addition, provide an option that allows the user to exit the purchasing loop at any time.

budget=int(input("Enter budget for lunch"))
apple=50
cake=100
bread=10
total=0
def Total(qty,price):
 total=qty*price
 return total

def amt(budget,total):
	if(budget<total):
		print("---------------------------------------------")
		print("total is exceeding")
		print("---------------------------------------------")
		exit();
	else:	
		budget=budget-total
		print("-------------------Remaining budget----------")
		print("remaining budget is {}".format(budget))
		print("---------------------------------------------")


while(True):
 print("      Item        |   Price")
 print(" 1.1kg Apples     |   50")
 print(" 2.1 Cake         |   100 ")
 print(" 3.1 Bread        |   10")
 print("              4. Exit     ")


 choice=int(input("enter choice"))

 if choice==1:

     n=int(input("enter quantity"))

     total=total+Total(n,50)
     amt(budget,total)
     print("total of {} Apples are{}".format(n,total))
 elif choice==2:

     n=int(input("enter quantity"))
     total=(total+Total(n,100))
     amt(budget,total)
     print("total of {} cake is{}".format(n,total))

 elif choice==3:
     n=int(input("enter quantity"))
     total=total+Total(n,10)
     amt(budget,total)
     print("total of {} bread is{}".format(n,total))

 
 else:
     break;


print("net total is {}".format(total))