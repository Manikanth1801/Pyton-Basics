# Example of for loop with range
print("For loop with range:")
for i in range(5):
    print(i)  # This will print numbers from 0 to 4

# Example of enumerate in for loop
print("\nEnumerate in for loop:")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)  # This will print the index and the fruit

# Example of while loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count)  # This will print numbers from 0 to 4
    count += 1

# Example of break in loop
print("\nBreak in loop:")
for i in range(10):
    if i == 5:
        break  # This will exit the loop when i is 5
    print(i)  # This will print numbers from 0 to 4

# Example of continue in loop
print("\nContinue in loop:")
for i in range(10):
    if i % 2 == 0:
        continue  # This will skip the rest of the loop when i is even
    print(i)  # This will print odd numbers from 1 to 9