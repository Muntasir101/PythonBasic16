print("Hello world!")

for _ in range(2):
    print("Dhaka")

# Iterating over a Range
for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

"""
lower limit and upper limit  and 
print only Even numbers
"""

lower_limit = int(input("Lower limit: "))
upper_limit = int(input("Upper limit: "))

for i in range(lower_limit, upper_limit):
    if i % 2 == 0:
        print(i)
