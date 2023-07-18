def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
num_list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input("Enter element {}: ".format(i + 1)))
    num_list.append(num)
sort_list(num_list)
print("Sorted list:", num_list)
