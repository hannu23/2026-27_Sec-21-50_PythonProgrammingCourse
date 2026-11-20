
total_numbers = int(input("Enter  many numbers: "))

largest = float(input("Enter a number: "))

for count in range(total_numbers - 1):
    number = int(input("Enter a number: "))
    if number > largest:
        largest = number

print(f"Largest among {total_numbers} numbers is {largest}")