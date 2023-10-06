"""
name = input('Enter Name: ')
age = int(input('Enter age: '))

user_details = []

# user_details.append(name)
# user_details.append(age)


user_details.extend([age, name])

print(user_details)
"""

"""
numbers = []
even_numbers = []
odd_numbers = []

for i in range(10):
    numbers.append(i)
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(numbers)
print(even_numbers)
print(odd_numbers)
"""

"""
username_list = ['admin', 'super admin', 'user']
password_list = ['1234', '123']

username = input("Enter Username: ")

if username in username_list:
    print("User Found")
    
    password = input("Enter Password: ")
    
    if password in password_list:
        print("Login Successful.")
    else:
        print("Incorrect Password.Login Failed.")
else:
    print("User not found.")

"""
cities = []

for i in range(5):
    city = input("Enter City name: ")
    cities.append(city)

print(cities)
