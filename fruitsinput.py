fruits_catalog = ("apple", "banana", "mango", "orange", "grapes", "kiwi", "pineapple")

stock = {"apple", "mango", "orange", "kiwi"}

fruit_name = input("Enter the name of a fruit: ").lower()


if fruit_name in fruits_catalog:
    if fruit_name in stock:
        print(f"{fruit_name.capitalize()} is available in stock.")
    else:
        print(f"{fruit_name.capitalize()} is sold here, but currently out of stock.")
else:
    print(f"{fruit_name.capitalize()} is not sold in this shop.")
