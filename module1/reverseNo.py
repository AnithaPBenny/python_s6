n = int(input("Enter a no.: "))
rev = 0
sum = 0
while n > 0:
    rem = n % 10
    n = n//10
    rev = rev*10 + rem
    sum += rem
print("reverse No: ", rev)
print("sum of digits: ", sum)