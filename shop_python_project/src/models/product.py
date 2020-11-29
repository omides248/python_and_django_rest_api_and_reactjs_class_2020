from itertools import count as itertools_count
from src.models.category import Category


class Product:
    __table = [
        {'id': '1', 'name': 'shoes_sport', 'price': 200000, 'category_id': '1', 'off': 2.0},
        {'id': '2', 'name': 'shoes_sport', 'price': 200000, 'category_id': '1', 'off': 2.0}
    ]
    __id = itertools_count(1)

    @classmethod
    def get_all_products(cls) -> list:
        return cls.__table

    @classmethod
    def get_one_product(cls, _id: str = None) -> dict:

        if not _id:
            return {}

        for product in cls.__table:
            if _id == product.get("id"):
                return product

        return {}

    @classmethod
    def save(cls, name: str = None, price: int = None, category_name: str = None, off: float = None) -> (bool, str):

        if not name or not price or not category_name or not off:
            return False, f"name: {name} or price: {price} or category: {category_name} or off: {off} not found"

        for category in Category().get_all_categories():
            if category.get("name") == name:
                cls.__table.append(
                    dict(
                        id=str(next(Product.__id)),
                        name=name,
                        price=price,
                        category_id=category.get("id"),
                        off=off
                    )
                )
                return True, ""

        return False, "category not found"

    @classmethod
    def update(cls, _id: str = None, name: str = None, price: int = None, category_name: str = None,
               off: float = str) -> (bool, str):

        ctg = {}
        if category_name:
            ctg = Category.get_one_category_with_name(category_name)
            if not ctg:
                return False, f"category_name: {category_name} not found"

        product = cls.get_one_product(_id)

        if product:

            if category_name:
                product["category_id"] = ctg.get("id")

            if name:
                product["name"] = name

            if price:
                product["price"] = int(price)

            if off:
                product[off] = float(off)

            return True, ""

        return False, f"product not found with id: {_id}"

    @classmethod
    def delete(cls, _id: str = None) -> (bool, str):
        if not _id:
            return False, "_id not found"

        for product in cls.__table:
            if _id == product.get("id"):
                cls.__table.remove(product)
                return True, f"Successfully remove product with id: {_id}"

        return False, f"product not found with id: {_id}"
