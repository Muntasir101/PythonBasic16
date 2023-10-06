my_list = [1, 2, 3]

# append()
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# extend()
my_list.extend([5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# insert()
my_list.insert(0, 0)
print(my_list)  # [0, 1, 2, 3, 4, 5, 6]

# remove()
my_list.remove(6)
print(my_list)  # [0, 1, 2, 3, 4, 5]

# pop(i)
popped_item = my_list.pop(1)
print(popped_item)
print(my_list)

# count()
new_list = [11, 21, 11, 33, 44, 54, 11, 21]
count = new_list.count(33)
print(count)

# length
print(len(new_list))

# Sort(): ascending
new_list.sort()
print(new_list)  # [11, 11, 11, 21, 21, 33, 44, 54]

# reverse
new_list.reverse()
print(new_list)  # [54, 44, 33, 21, 21, 11, 11, 11]
