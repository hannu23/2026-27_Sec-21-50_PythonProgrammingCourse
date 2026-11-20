# Example solution: Fibonacci series up to N terms using a for loop
n = int(input("Enter how many terms: "))

one = 0
two = 1

for count in range(n):
    print(f"Fibonacci series term {count + 1} of {n} terms = {one}")
    next_term = one + two   
    one = two
    two = next_term