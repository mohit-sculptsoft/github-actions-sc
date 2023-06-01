# app.py

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Testing the functions
print(add_numbers(5, 3))
print(subtract_numbers(10, 4))
print(multiply_numbers(6, 2))
print(divide_numbers(10, 2))
print(divide_numbers(8, 0))
