# Fernando Valadez-Nunez
# 02/20/2020

# Problem 5 - Write a program to compute the conversion given a user input value
# Print this value as well as the calculated value using the degrees function
# in the math module

import math

pi=22/7

radian = float(input("Input radians: "))

degree = radian*(180/pi)

print("Degree:",degree)
