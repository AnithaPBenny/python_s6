def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant 1"
    elif x < 0 and y > 0:
        return "Quadrant 2"
    elif x < 0 and y < 0:
        return "Quadrant 3"
    elif x > 0 and y < 0:
        return "Quadrant 4"
    else:
        return "Origin"

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

quadrant = find_quadrant(x, y)
print("The point ({}, {}) is in {}".format(x, y, quadrant))
