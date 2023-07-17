import math

def calculate_sin(x, n):
    radian = math.radians(x)
    sin_value = 0
    for i in range(n):
        term = ((-1) ** i) * (radian ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sin_value += term
    return sin_value
x = float(input("Enter the value of x in degrees: "))
n = int(input("Enter the number of terms (n): "))
result = calculate_sin(x, n)
print(result)
