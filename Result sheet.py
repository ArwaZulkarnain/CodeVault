 ### Function...... is a block of code that runs only when we call it
def greet():
    print("Hello, Welcome to the program")
### Sum of 5 numbers
def sum(a, b, c, d, e):
    print("Sum of 5 numbers")
    total = a + b + c + d + e
    print("Sum:", total)
    return total  
### Calculate average and percentage
def avg_marks(a, b, c, d, e):
    print("Calculate average of your result")
    total = a + b + c + d + e
    average = total / 5
    print("Average:", average)
    percentage = (total / 500) * 100
    print("Percentage:", percentage, "%")
    return percentage 
### now assigning the grade acc to numbers
def assign_grade(percentage):
    print("Assigning Grade...")
    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
greet()
sum(100, 100, 100, 100, 100)
### Take the input from user
a = int(input("Enter your marks of English:"))
b = int(input("Enter your marks of Mathematics:"))
c = int(input("Enter your marks of Chemistry:"))
d = int(input("Enter your marks of Biology:"))
e = int(input("Enter your marks of Physics:"))
total = sum(a, b, c, d, e)
percentage = avg_marks(a, b, c, d, e)
assign_grade(percentage)
