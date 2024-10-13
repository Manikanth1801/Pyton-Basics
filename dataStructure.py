# Description: This file contains the basic data structures in Python.

# Lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", True]

first_element = numbers[0] #`1`
last_element = numbers[-1] #`5`
sublist = numbers[1:3]  # [2, 3]
length = len(numbers) # 5

#modify list
numbers.append(6) # [1, 2, 3, 4, 5, 6]
numbers.insert(1, 0, 5) # [1, 0, 5, 2, 3, 4, 5, 6]
numbers.remove(0) # [1, 5, 2, 3, 4, 5, 6]
numbers.pop() # [1, 5, 2, 3, 4, 5]

# Tuples
empty_tuple = ()
point = (2, 3)  
print(point)  # This will print (2, 3)
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple) # ('apple', 'banana', 'cherry')

# Accessing elements in a tuple
first_element = point[0]  # 2
second_element = point[1]  # 3

# Tuples are immutable, so you cannot modify them directly
# point[0] = 5  # This will raise a TypeError

# You can concatenate tuples
new_point = point + (4, 5)  # (2, 3, 4, 5)

# You can create a new tuple from existing tuples
combined_tuple = point + thistuple  # (2, 3, 'apple', 'banana', 'cherry')

# You can repeat tuples
repeated_tuple = point * 2  # (2, 3, 2, 3)

# You can check for membership
is_in_tuple = 'apple' in thistuple  # True

# You can find the length of a tuple
tuple_length = len(thistuple)  # 3

# You can iterate through a tuple
for item in thistuple:
    print(item)

