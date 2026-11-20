total_numbers=int(input("Enter the choice numbers: "))
total_sum=0
for count in range(total_numbers):
    number=int(input("Enter the number: "))
    total_sum+=number
    
    average=total_sum/total_numbers
    print(f"The sum of the numbers is: {total_sum}")
    print(f"The average of the numbers is: {average}")