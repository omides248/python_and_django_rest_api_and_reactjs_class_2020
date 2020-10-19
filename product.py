class Product:
    __products_db = []

    def __init__(self, name, price, category, off):
        self.name = name
        self.price = price
        self.category = category
        self.off = off

    def add_product(self):
        self.__products_db.append(self)

    @classmethod
    def get_products_db(cls):
        # print(cls.products_db)
        return cls.__products_db

    def __repr__(self):
        return self.name


shoes_product_obj = Product("shoes", 200000, "cloths", 23)
shoes_product_obj.add_product()
# shoes_product_obj.show()

bag_product_obj = Product("bag", 180000, "cloths", 2.1)
bag_product_obj.add_product()
# bag_product_obj.show()


# products = Product.get_products_db()
#
# for product in products:
#     print(product)
#     print(product.off)
#     print("------------")


# print(Product.__products_db)
