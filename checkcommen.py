common_element = int(input("Enter a number to check: "))
my_list = [1, 2, 3, 4, 5]
my_set = {4, 5, 6, 7}

if common_element in my_list and common_element in my_set:
    print(f"{common_element} is common to both list and set.")
else:
    print(f"{common_element} is not common to both list and set.")
