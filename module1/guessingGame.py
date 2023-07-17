import random
low = int(input("Enter a lower range: "))
high = int(input("Enter a higher range: "))
guessNumber = random.randint(low, high)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter a number: "))
    if userNumber < guessNumber:
        print("Too small")
    elif userNumber > guessNumber:
        print("Too big")
    else:
        print("Congratulations! you got the number in ", count, " tries")
        break