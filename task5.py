# ---------------------------------------------
# Prime Number Checker
# Author: [Your Name]
# Description:
# This program checks if a given number is prime or not.
# ---------------------------------------------

num = int(input("Enter a number to check if it is prime: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
