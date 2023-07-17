binary = input("Enter a binary number: ")
decimal = 0
exponent = len(binary)-1
for i in binary:
    decimal = decimal + int(i)*2**exponent
    exponent -= 1
print("Decimal equivalent: ", decimal)
