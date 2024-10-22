import math


def parse_equation(equation):

    equation = equation.replace(" ", "").strip()

    a_str = equation.split('x^2')[0]

    b_c_part = equation.split('x^2')[1]

    b_str = b_c_part.split('x')[0]

    c_str = b_c_part.split('x')[1] \
        .split('=')[0]

    convert_map = {'': 1, '+': 1, '-': -1}

    def convert(x):
        return convert_map.get(x, int(x))

    a = convert(a_str)
    b = convert(b_str)
    c = convert(c_str)

    return a, b, c


def solve_quadratic(a, b, c):

    discriminant = b**2 - 4*a*c
    sqrt_discriminant = math.sqrt(abs(discriminant))
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)

    return root1, root2


equation = input("Enter a equation in the format ax^2 + bx + c = 0: ")
a, b, c = parse_equation(equation)

# Solve the equation
root1, root2 = solve_quadratic(a, b, c)

# Output the results
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
