from src.models.product import Product
from src.views.category_view import CategoryView
from src.views.login_logout_view import LoginLogoutView
from src.views.register_view import RegisterView


class MenuView:
    menu = {
        "1": " Add product",
        "2": " Show product",
        "3": " Update product",
        "4": " Delete products",

        "5": " Add Category",
        "6": " Show categories",
        "7": " Update category",
        "8": " Delete category",

        "9": " Show users",
        "10": "Register customer",
        "11": "Register employee",

        "12": "Buy products",
        "13": "Show orders",
        "14": "export csv of orders ( ./csv/datetime/*.csv )",

        "15": "login",
        "16": "logout",

        "17": "show menu",

        "0": "exit",
    }

    @classmethod
    def show_menu(cls):
        print("---------- Welcome ----------")
        for num, title in cls.menu.items():
            if num in ("5", "9", "13", "17", "0"):
                print("************************")
            print(f"{num}: {title}")

    @classmethod
    def show(cls):

        print("---------- Welcome ----------")
        for num, title in cls.menu.items():
            if num in ("5", "9", "13", "17", "0"):
                print("************************")
            print(f"{num}: {title}")

        print("*****************************")
        user_input = input("Enter your number:")

        while True:

            if user_input == "1":
                name = input("name: ")
                price = int(input("price: "))
                category = input("category: ")
                off = float(input("off: "))
                result, err = Product.save(name, price, category, off)
                if result:
                    print("Successfully add product")
                else:
                    print(err)

            if user_input == "2":
                print(Product.get_all_products())

            if user_input == "3":
                products_fields = ["id", "name", "price", "category_name", "off"]
                _id, name, price, category_name, off = [input(f"{field}:") for field in products_fields]
                print(_id, name, price, category_name, off)
                result = Product.update(_id, name, price, category_name, off)
                if result:
                    print("Successfully update product")
                else:
                    print("Update err")

            if user_input == "4":
                result, err = Product.delete(input("id: "))
                if result:
                    print("Successfully delete")
                else:
                    print(err)

            if user_input == "5":
                CategoryView.add_category()

            if user_input == "6":
                CategoryView.show_all()

            if user_input == "7":
                a, b = CategoryView.update_category()
                print(a, b)

            if user_input == "8":
                CategoryView.delete_category()

            if user_input == "9":
                RegisterView.create_customer()

            if user_input == "10":
                RegisterView.create_employee()

            if user_input == "16":
                LoginLogoutView.login()

            user_input = input("Enter your number:")
