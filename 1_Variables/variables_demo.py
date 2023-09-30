"""
Data Types:
1. Numeric(integer, float)
2. Sequence(string, list, tuple)
3. Boolean
4. Mapping(Dictionary)
5. Set
"""
number2 = 10
tax = 10.3

# Sequence(string, list, tuple)
name = 'Mr.Smith'
email = "test@mail.com"

product_id = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
employee_id = (1, 2, 3, 4, 5)  # tuple

# Boolean
login_status = True
active = True

# Mapping(Dictionary)
# key : Value
user_details = {
    "name": "Mr. Smith",
    "email": "test@mail.com",
    "active": True,
    "phone": 1233,
    "passwords": [123, 1234, 324324, 333],
    "address": {
        "address_present": {
            "present_address": "Dhaka",
            "road": 12
        },
        "address_permanent": {
            "permanent_address": "NY",
            "road": 1234
        }
    }
}

# Set
group1 = {12, 33, 44, 43}
group2 = {23, 34, 543}

cites = ["dhaka", "ctg", "rajshahi"]
print(cites)