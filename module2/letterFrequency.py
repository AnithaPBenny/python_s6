def list_of_frequency(inputString):
    freq = {}  # dictionary to store word and its count
    frequency = inputString.lower()
    for item in frequency:
        if item in freq:
            freq[item] += 1  # item already in the dictionary , increment the count
        else:
            freq[item] = 1
    print(freq)


inputString = input("Enter a string: ")
list_of_frequency(inputString)
