# String: sequence of characters that have quote in open and end

txt = 'Hello World'
print(txt[1])
print(txt[1:5])
print(txt[1:])
print(txt[:-1])

# stripe()
message = " rain "
print(message.strip())

# upper()
description = "New year"
print(description.upper())

# lower
print(description.lower())

# Length
print(len(description))

# Formatting
name = "Red"
# option 1
print("Hello! My name is Smith")

# option 2
print("Hello! My name is ", name)

# option 3
city = input("Enter City: ")
age = int(input("Enter Age: "))
greetings = "Hello! My City is {}"
print(greetings.format(city))

# option 4
print(f"Hello! My City is {city} and my age {age}")
