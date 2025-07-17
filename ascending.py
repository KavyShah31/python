tuple_input = input("Enter tuple elements (space-separated): ")
my_tuple = tuple(int(x) for x in tuple_input.split())

if my_tuple == tuple(sorted(my_tuple)):
    print("The tuple is sorted in ascending order.")
else:
    print("The tuple is NOT sorted in ascending order.")
