P= float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (in %): "))
T = float(input("Enter the time (in years): "))

A = P * (1 + R / 100) ** T
compound_interest = A - P

print("The Compound Interest is:", compound_interest)
print("The Total Amount after", T, "years is:", A)
