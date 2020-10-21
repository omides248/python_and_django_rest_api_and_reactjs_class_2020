import itertools
from category import Category


class Product:
    __db = []
    __id = itertools.count(1)

    def save(self, name=None, price=None, category=None, off=None):
        ctg = Category().exits(category)
        if ctg:
            g = {
                "id": next(Product.__id),
                "name": name,
                "price": int(price),
                "category_id": ctg.get("id"),
                "off": float(off)
            }
            self.__db.append(g)
            return True
        else:
            return False

    @classmethod
    def get_products_db(cls):
        # print(cls.products_db)
        return cls.__db

    def __repr__(self):
        return self.name

    def delete(self, id):
        for product in self.__db:
            if id == product.__id:
                self.__db.remove(product)

    # def update(self, id):
    #     for product in self.__db:
    #         if id == product.__id:
    #             if name:
    #                 product.name = name

# shoes_product_obj = Product("shoes", 200000, "cloths", 23)
# shoes_product_obj.add_product()
# shoes_product_obj.show()

# bag_product_obj = Product("bag", 180000, "cloths", 2.1)
# bag_product_obj.add_product()
# bag_product_obj.show()
# print(shoes_product_obj.id)
# print(bag_product_obj.id)

# products = Product.get_products_db()
#
# for product in products:
#     print(product)
#     print(product.off)
#     print("------------")


# print(Product.__products_db)

# g = itertools.count(1, 2)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
