decimal = int(input("Enter a decimal number: "))
if decimal == 0:
    print("Binary equivalent: 0")
else:
    binary = ""
    while decimal > 0:
        reminder = decimal % 2
        decimal = decimal // 2
        binary = str(reminder) + binary
    print("Binary equivalent: ", binary)
