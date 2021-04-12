# This script is literally because normal calculators don't do exponents without a hassle

# Imports
import time

# User input for variables and terms
function = input("What is the function: ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")


# Loops for each operation (five functions)
if function == "+":
    print(int(num1)+int(num2))
    time.sleep(5)
elif function == "-":
    print(int(num1)-int(num2))
    time.sleep(5)
elif function == "*":
    print(int(num1)*int(num2))
    time.sleep(5)
elif function == "/":
    print(int(num1)/int(num2))
    time.sleep(5)
elif function == "^":
    print(int(num1)**int(num2))
    time.sleep(5)
