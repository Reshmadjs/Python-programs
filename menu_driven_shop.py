# Write a simple menu driven program for a shop, which sells the following items:
# The user selects items using a menu. For every item selected, ask the quantity. If the quantity of
# any item is more than 10, give a discount of _____%. When the user selects Exit, display the
# total amount.
total=0
def Total(qty,price):
 total=qty*price
 return total

while(True):
 print("      Item        |   Price")
 print(" 1.keyboard       |   1000")
 print(" 2.mouse          |   500")
 print(" 3.monitor        |   32000")
 print(" 4.laptop         |   50000")
 print(" 5.cpu            |   1300")
 print("              6. Exit     ")


 choice=int(input("enter choice"))

 if choice==1:

     n=int(input("enter quantity"))
     total=total+Total(n,1000)
     print("total of {} keyboard is{}".format(n,total))
 elif choice==2:

     n=int(input("enter quantity"))
     total=(total+Total(n,500))
     print("total of {} mouse is{}".format(n,total))

 elif choice==3:
     n=int(input("enter quantity"))
     total=total+Total(n,32000)
     print("total of {} monitor is{}".format(n,total))

 elif choice==4:
     n=int(input("enter quantity"))
     total=total+Total(n,50000)
     print("total of {} laptop is{}".format(n,total))

 elif choice==5:
     n=int(input("enter quantity"))
     total=total+Total(n,1300)
     print("total of {} cpu is{}".format(n,total))

 else:
     break;


print("net total is {}".format(total))