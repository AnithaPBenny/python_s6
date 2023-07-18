inputString = input("Enter the string:")
li = inputString.split()  # converts the string into the list of words
freq = {}  # dictionary to store word and its count
for item in li:
    if item in freq:
        freq[item] += 1  # item already in the dictionary , increment the count
    else:
        freq[item] = 1
print(freq)
