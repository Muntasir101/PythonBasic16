"""
if condition:
    code
else:
    code
"""

number = 1

if number > 10:
    print("Good")
else:
    print("Hello")

#marks = 10

marks = int(input("Enter your marks: "))

if marks < 30:
    print("Grade F")
elif 30 <= marks < 40:
    print("Grade D")
elif 40 <= marks < 50:
    print("Grade C")
elif 50 <= marks < 60:
    print("Grade B")
elif 60 <= marks < 70:
    print("Grade A-")
elif 70 <= marks < 80:
    print("Grade A")
elif 80 <= marks <= 100:
    print("Grade A+")
else:
    print("Invalid Marks")

"""
Discount feature: If customer 
purchase less than 1000 will get 5% discount.
purchase less than 2000 will get 10% discount.
purchase more than 2000 will get 20% discount.
Ask user to input purchase amount. 
"""

purchase_amount = int(input("purchase amount: "))

if purchase_amount < 1000:
    print("Discount 5%")
elif 1000 <= purchase_amount < 2000:
    print("Discount 10%")
elif purchase_amount >= 2000:
    print("Discount 20%")
else:
    print("Invalid Purchase Amount")

"""
Calculator: User input 2 numbers and choose operator(+,-,*,/)
System will calculate the result. 
"""
number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))
operator = input("operator: (+,-,*,/): ")

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Invalid input")

