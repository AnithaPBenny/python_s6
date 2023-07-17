def separate_numbers():
    n = int(input("Enter the number of integers: "))
    numbers = []
    positive_numbers = []
    negative_numbers = []
    print("Enter the numbers")
    for i in range(n):
        number = int(input(""))
        numbers.append(number)
        if number > 0:
            positive_numbers.append(number)
        elif number < 0:
            negative_numbers.append(number)
    return positive_numbers, negative_numbers
positive_nums, negative_nums = separate_numbers()
print("Positive numbers:", positive_nums)
print("Negative numbers:", negative_nums)
