import re
import math

def extract_coefficients(equation):
    # Remove all spaces and convert '^' to '**'
    equation = equation.replace(" ", "").replace("^", "**")
    
    # Pattern to find the coefficients
    pattern = r'([-+]?\d*\.?\d*)x?\*?\*?2?([-+]?\d*\.?\d*)x?([-+]?\d*\.?\d*)'
    
    match = re.match(pattern, equation)
    if match:
        a, b, c = match.groups()
        
        # Convert coefficients to float, handling special cases
        a = float(a) if a and a not in ['+', '-'] else (1 if a in ['', '+'] else -1)
        b = float(b) if b and b not in ['+', '-'] else (1 if b == '+' else -1 if b == '-' else 0)
        c = float(c) if c else 0
        
        return a, b, c
    else:
        return None

def solve_quadratic_eq(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check the value of the discriminant
    if discriminant < 0:
        return "The equation has no real roots."
    elif discriminant == 0:
        x = -b / (2*a)
        return f"The equation has one real root: x = {x:.2f}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The roots of the equation are: x1 = {x1:.2f} and x2 = {x2:.2f}"

# User interface
print("Enter a quadratic equation in the format ax^2 + bx + c")
print("For example: 2x^2 - 3x + 1 or 2x^2-3x+1")
equation = input("Enter the equation: ")

coefficients = extract_coefficients(equation)
if coefficients:
    a, b, c = coefficients
    print(f"Identified coefficients: a = {a}, b = {b}, c = {c}")
    result = solve_quadratic_eq(a, b, c)
    print(result)
else:
    print("Invalid equation format. Please check your input.")
