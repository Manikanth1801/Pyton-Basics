# Define the greet function that takes a name as a parameter
def greet(name):
    return f"Hello, {name}!"

# Call the greet function with a specific name and print the result
print(greet("Alice"))  # This will print "Hello, Alice!"

# Take input from the user for the name
user_name = input("Enter your name: ")

# Call the greet function with the user-provided name and print the result
print(greet(user_name))  # This will print "Hello, <user_name>!"

# default params
def greet2(name, message="Hello"):
    return f"{message}, {name}!"

print(greet2("Alice"))  # This will print "Hello, Alice!"

# variable length args
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))  # This will print 6

#keyword args
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30)

#return type
def get_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    initials = f"{first_name[0]}{last_name[0]}"
    return full_name, initials

name, initials = get_full_name("John", "Doe")
print(name)  # This will print "John Doe"
print(initials)  # This will print "JD"
print(get_full_name("Alice", "Smith"))  # This will print ("Alice Smith", "AS")