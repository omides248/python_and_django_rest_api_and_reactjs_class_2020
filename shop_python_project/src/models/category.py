from itertools import count as itertools_count

from src.session.session import Session


class Category:
    __table = [{'id': '1', 'name': 'shoes'}]
    __id = itertools_count(1)

    @classmethod
    def get_all_categories(cls) -> list:
        return cls.__table

    @classmethod
    def get_category_with_id(cls, _id: str = None) -> dict:
        if not _id:
            return {}

        for category in cls.__table:
            if _id == category.get("id"):
                return category

        return {}

    @classmethod
    def get_one_category_with_name(cls, name: str = None) -> dict:
        if not name:
            return {}

        for category in cls.__table:
            if name == category.get("name"):
                return category

        return {}

    @classmethod
    def save(cls, name: str = None) -> (bool, str):

        if not name:
            return False, "name is empty"

        if cls.exits_with_name(name):
            return False, "Category exists with name"

        cls.__table.append({"id": str(next(cls.__id)), "name": name})
        return True, ""

    @classmethod
    def update(cls, _id: str = None, name: str = None) -> bool:

        category = cls.get_category_with_id(_id)

        if category:
            if name:
                category["name"] = name

            return True

        return False

    @classmethod
    def delete(cls, _id: str = None) -> (bool, str):
        if not _id:
            return False, "id not found in params"

        # TODO check products does not use this category

        for category in cls.__table:
            if category.get("id") == _id:
                return (True, "") if cls.__table.remove(category) else (False, f" category with id: {_id} not found")
        return False, "category not found for update"

    @classmethod
    def exits_with_id(cls, name: str = None) -> bool:
        if not name:
            return False

        for category in cls.__table:
            if category.get("id") == id:
                return True
        return False

    @classmethod
    def exits_with_name(cls, name: str = None) -> bool:
        if not name:
            return False

        for category in cls.__table:
            if category.get("name") == name:
                return True
        return False
