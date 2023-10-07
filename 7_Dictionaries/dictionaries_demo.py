user_details = {
    "name": "Mr. Smith",
    "email": "test@mail.com",
    "active": True,
    "phone": 1233,
    "passwords": [123, 1234, 324324, 333],
    "address": {
        "address_present": {
            "city": "Dhaka",
            "road": 12,
            "house":{
                "house_id": 123,
                "house_name": "Super House"
            }
        },
        "address_permanent": {
            "city": "NY",
            "road": 1234
        }
    }
}
print(type(user_details))

# length
print(len(user_details))
print(len(user_details['address']))

# Extract item
user_name = user_details['name']
print(user_name)

print(user_details.get('name'))

# Extract nested item
city = user_details['address']['address_permanent']['city']
print(city)

house_name = user_details['address']['address_present']['house']['house_name']
print(house_name)

# get all key
all_keys = user_details.keys()
print(all_keys)

# get all values
all_values = user_details.values()
print(all_values)

# add new key
user_details['favorite_sports'] = 'Cricket'
print(len(user_details))

print(user_details)

# update value
user_details['favorite_sports'] = 'Football'
print(user_details)

# delete key
user_details.pop('favorite_sports')

all_keys = user_details.keys()
print(all_keys)

# clear dictionary
user_details.clear()

print(user_details)

print(type(user_details))