my_list = [1, 2, 3, 4, 5]
my_set = {4, 5, 6, 7}

# Convert list to set and check intersection
common_elements = set(my_list) & my_set

if common_elements:
    print(f"Common elements found: {common_elements}")
else:
    print("No common elements found")
