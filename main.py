1#class declaration,module and variables
import sys
class hotelmanage:
  
  def __init__(self, rt="", s=0, p=0, r=0, t=0, a=1000, name="", address="", cindate="", rno=1):
    print(" *** WELCOME TO HOTEL KIPII***")
    self.rt=rt
    self.r=r
    self.t=t
    self.p=p
    self.s=s
    self.a=a
    self.name=name
    self.address=address
    self.cidate=cindate
    self.coutdate=coutdate
    self.rno=rno

#customer information

def inputdata(self):
  self.name=input("\n Enter your Fullname:")
  self.address=input("\n Enter your address:")
  self.cindate=input("\n Enter your check in date:")
  self.coutdate=input("\n Enter your check out date:")

  print("Yur room no.:",self.rno,"\n")
  
#room rent
  
def roomrent(self):#sel1353  
  print("we have the following rooms:-")
  print("1. Class A-->4000")
  print("2. Class B-->3000")
  print("3. Class C-->2000")
  print("4. Class D-->1000")

  x=int(input("Enter the number of your  choice please->"))
  n=int(input("For How Many Nights Did You Stay:"))
  if(x==1):
    print("you have chosed room Class A")
    self.s= 4000*n

  elif(x==2):
      print("you have choosen room Class B")
      self.s=3000*n
  elif(x==3):
  
      print("you have choosen room Class C")
      self.s=2000*n
  elif(x==4):
      print("you have choosen room Class D")
      self.s=1000*n

  else:
      print("please choose a room")
      print("your choosen room rent is=\n",self.s)

#food module
      
def foodpurchased(self):
  print("***AVAILABLE MENU***")
if ("1=Dessert"):
  price =100
elif("2=Drinks"):
  price=50;
elif("3=Breakfast"):
  price=90
elif("4=Lunch"):
  price=110
elif("5=Dinner"):
  price=150;
else:
  print("6.Exit")
  # print("1.Dessert",price=100)
  # print("2.Drinks", price=50)
  # print("3.Breakfast",price=90)
  # print("4.Lunch", price=110)
  # print("5.Dinner",price=150)
  # print("6.Exit")
c=int(input("Enter the number of your choice:"))
d=int(input("Enter the quantity:"))
cost = d*price
print(cost)

if(c==1):
  print("Dessert")
  print(cost)

elif(c==2):
  print("Drinks")
  print(cost)
elif(c==3):
  print("Breakfast")
  print(cost)
elif(c==4):
  print("Lunch")
  print(cost)
elif(c==5):
  print("Dinner")
  print(cost)
elif(c==6):
  sys.exit()
else:
  print("you have entered an invalid key")
  print("Total food Cost=Rs",self.r,"\n")



# while(1):
#     c=int(input("Enter the number of your choice:"))
      
  
#     def __init__(self):
#         print("Address of self = ",id(self))
# if(c==1):
#     d=int(input("Enter the quantity:"))
#     self.r=self.r+100*d
# elif(c==2):
#     d=int(input("Enter the quantity:"))
#     self.r=self.r+50*d
# elif(c==3):
#     d=int(input("Enter the quantity:"))
#     self.r=self.r+90*d
# elif(c==4):
#     d=int(input("Enter the quantity:"))
#     self.r=self.r+110*d
# elif(c==5):
#     d=int(input("Enter the quantity:"))
#     self.r=self.r+150*d

# elif(c==6):
#     sys.exit()
# else:
#     print("you have entered an invalid key")
#     print("Total food Cost=Rs",self.r,"\n")

# #Billing module

def display(self):
  print("****TOTAL BILL****")
  print("Customer details:")
  print("Customer name:",self.name)
  print("Customer address:",self.address)
  print("Check in date:",self.cindate)
  print("Check out date:",self.coutdate)
  print("Room no.",self.rno)
  print("Your Room rent is:",self.s)
  print("Your Food bill is:",self.r)

  self.rt=self.s+self.t+self.p+self.r
  print("Your sub total Purchased is:",self.rt)
  print("Additional Service Charges is", self.a)
  print("Your grandtotal Purchased is:",self.rt+self.a,"\n")
  self.rno+=1

#main module

def main():
  while (1):
    print("1.Enter Customer Data")
    print("2.Calculate Room Rent")
    print("3.Calculate food purchased")
    print("4.Show total cost")
    print("5.Exit")
    b=int(input("\nEnter the number of your choice:"))

# a=hotelmanage()

# if (b==1):
#   a.inputdata()
# if (b==2):
#   a.roomrent()
# if (b==3):
#   a.foodpurchased()
# if (b==4):
#   a.display()
# if (b==5):
#    quit()
    main()

  

  





  






      



