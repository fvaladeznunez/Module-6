# Fernando Valadez-Nunez
# 02/20/2020

# Problem 6 - Use a for statement to calculate the factorial of a user input x
# value. Print this value as well as the calculated value using the factorial
# function in the math module.

import math

num = int(input("Enter a number: "))

fac = 1

for i in range(1, num + 1):
    fac = fac * i

print("Factorial of ", num, " is ", fac)
