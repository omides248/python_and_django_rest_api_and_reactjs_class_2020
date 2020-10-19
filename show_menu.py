a = {
    "1": "Add product",
    "2": "Update product",
    "3": "Delete product",
    "4": "Retrieve products",
    "5": "Add Category",
    "6": "Retrieve categories",
}

print("---------- Welcome ----------")
for num, title in a.items():
    print(f"{num}: {title}")

print("*****************************")
user_input = input("Enter your number:")
