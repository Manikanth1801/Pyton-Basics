# Dictionary
# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: John

# Adding a new key-value pair
person["email"] = "john@example.com"

# Updating a value
person["age"] = 31

# Removing a key-value pair
del person["city"]

# Iterating through keys
for key in person:
    print(key, person[key])

# Checking if a key exists
if "name" in person:
    print("Name is present in the dictionary")

# Getting the length of the dictionary
print(len(person))  # Output: 3

# Using the get method to access values
print(person.get("email"))  # Output: john@example.com

# Clearing the dictionary
person.clear()

# Sets

# Creating a set
empty_set = set()
unique_numbers = {1, 2, 3, 2, 1}  # {1, 2, 3}
# Adding elements to a set
unique_numbers.add(4)
unique_numbers.add(5)

# Removing elements from a set
unique_numbers.remove(2)  # Raises KeyError if 2 is not present
unique_numbers.discard(3)  # Does not raise an error if 3 is not present

# Checking if an element is in the set
print(1 in unique_numbers)  # Output: True
print(2 in unique_numbers)  # Output: False

# Iterating through a set
for number in unique_numbers:
    print(number)

# Set operations
another_set = {3, 4, 5, 6}

# Union
union_set = unique_numbers.union(another_set)
print(union_set)  # Output: {1, 3, 4, 5, 6}

# Intersection
intersection_set = unique_numbers.intersection(another_set)
print(intersection_set)  # Output: {4, 5}

# Difference
difference_set = unique_numbers.difference(another_set)
print(difference_set)  # Output: {1}

# Symmetric difference
symmetric_difference_set = unique_numbers.symmetric_difference(another_set)
print(symmetric_difference_set)  # Output: {1, 3, 6}

# Clearing a set
unique_numbers.clear()