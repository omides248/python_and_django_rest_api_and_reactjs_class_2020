from product import Product
from category import Category

a = {
    "1": "Add Category",
    "2": "Update product",
    "3": "Delete product",
    "4": "Retrieve category",
    "5": "Add Category",
    "6": "Retrieve categories",
    "7": "Add product",
    "8": "get product"
}

print("---------- Welcome ----------")
for num, title in a.items():
    print(f"{num}: {title}")

print("*****************************")
user_input = input("Enter your number:")
print(user_input)
while True:

    if user_input == "1":
        name = input("name: ")
        if Category().save(name):
            print(f"success add category: {name}")
        else:
            print(f"This category exists with {name}")

    if user_input == "4":
        print(Category().get_all_category())

    if user_input == "7":
        name = input("name: ")
        price = input("price: ")
        category = input("category: ")
        off = input("off: ")
        res = Product().save(name, price, category, off)
        if res:
            print("yesssss")
        else:
            print(f"Please add category with {category}")
    if user_input == "8":
        print(Product().get_products_db())

    user_input = input("Enter your number:")
