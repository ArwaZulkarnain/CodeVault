import math
def add(a,b):
  return a+b 
    
    
def subtract(a,b):
  return a-b
    
def multiply(a,b):
  return a*b
def divide(a, b):
    if b == 0:
        return "Error! cannot divide be zero"
    return a/b
def square(a,b):
    return a**2
   
def cube(a,b):
    return a**3,
  
def percentage(a,b):
   if b==0:
      return "Error not divide"
   return a/b*100
def factorial(a):
    if a < 0 or not a.is_integer():
        return "Error! Factorial only defined for non-negative integers"
    return math.factorial(int(a))
def log_value(a):
    if a <= 0:
        return "Error! Logarithm undefined for zero or negative"
    return math.log10(a)
   
    
def show_menu():
    print("\n---Calculator app menu---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.square")
    print("6.cube")
    print("7.precentage")
    print("8.Factorial")
    print("9.log_value")
    print("10. Exit")
    
def calculator():
    while True:
        show_menu()
        choice = input("Enter your choice(1-10):")
        if choice == "10": 
          print("Exiting Calculator Goodbye :)")
          break
      
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
      
        if choice =="1":
          print("Result:", add(num1,num2))
        elif choice == "2":
          print("Result:", subtract(num1,num2))
        elif choice =="3":
          print("Result:", multiply(num1,num2))
        elif choice == "4":
          print("Result:", divide(num1,num2))
        elif choice=="5":
           print("Result:", square(num1,num2))
        elif choice=="6":   
           print("Result:", cube(num1,num2)) 
        elif choice=="7":
           print("Result:", percentage(num1,num2)) 
        elif choice=="8":
           print("Result:", factorial(num1)) 
        elif choice=="9":
           print("Result:", log_value(num1)) 
        else:
          print("Invalid input! Please choose from 1-10")
calculator()
