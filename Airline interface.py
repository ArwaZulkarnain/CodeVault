### Qatar Airlines Interface
print("Welcome to Qatar Airline")
print("We are moving from Pakistaan to Dubai")
### Choose the ticket class
print("Choose your ticket class")
print("1.Business class")
print("2.Economic class")
### take user output
choice = int(input("Enter 1. for Business class or 2. for economic class:"))
if choice == 1:
 print("\n you selected Business class")
 print("Luxury enviroment waiting for you")
elif choice == 2:
 print("\n you selected economic class")
 print("Have a Comfortable boarding")
else:
  print("\n invalid selection")
#### ask for passenger age in years
Age = int(input("\nEnter your age:"))
### price acc to thier age
if Age <= 3:
  price = 0
  print("You are Baby....no charges we will provide good service")
elif Age <= 12:
  price = 50000
  print("you are a child")
elif Age <= 18:
  price = 75000
  print("you are teenager")
else:
  price = 100000
  print("you are adult")
print(f"\nTicket price:RS.{price}")


print("Have a comfortable journey with us")


