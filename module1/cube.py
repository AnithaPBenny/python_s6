n = int(input("Enter a number: "))
sum = 0
for i in range(n):
    if i%2 == 0:
        result = i**3
        sum += result
print(sum)