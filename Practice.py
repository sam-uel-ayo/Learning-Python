# Summary of Key Concepts from Chapter 3

# Data Types
int_var = 42           # Integer
float_var = 3.14       # Floating-point
str_var = "Python"     # String

# Numeric Types and Operations
sum_result = int_var + float_var            # Addition
difference = int_var - float_var            # Subtraction
product = int_var * float_var               # Multiplication
quotient = int_var / float_var              # Division
exponentiation = int_var ** 2               # Exponentiation

# Using the Math Library
import math
sqrt_result = math.sqrt(int_var)            # Square root
log_result = math.log(float_var)            # Natural logarithm

# Loop Accumulator
accumulator = 0
for i in range(5):                          # Sum of first 5 numbers
    accumulator += i

# Bit Limits (demonstrated through max value check)
import sys
max_int = sys.maxsize                       # Maximum value of integer

# Type Conversion
int_to_float = float(int_var)               # Convert int to float
float_to_int = int(float_var)               # Convert float to int
str_to_int = int("123")                     # Convert string to int

# Print the results to illustrate the concepts
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Exponentiation: {exponentiation}")
print(f"Square root: {sqrt_result}")
print(f"Natural log: {log_result}")
print(f"Accumulator: {accumulator}")
print(f"Max integer value: {max_int}")
print(f"Int to float: {int_to_float}")
print(f"Float to int: {float_to_int}")
print(f"String to int: {str_to_int}")
