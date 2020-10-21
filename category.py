import itertools


class Category:
    __db = []
    __id = itertools.count(1)

    def save(self, name):
        # self.__db.append({"id": next(self.__id), "name": name})

        if not self.exits(name):
            id = next(self.__id)
            self.__db.append({"id": id, "name": name})
            return True
        else:
            return False

    def exits(self, name: str = None) -> dict:
        if name:
            # for category in self.get_all_category()
            for category in self.__db:
                if category.get("name") == name:
                    return category
            return {}
        else:
            return {}

    def delete(self, id):

        for num, category in enumerate(self.__db, 0):
            if category.get("id") == id:
                del self.__db[num]

        return True

    @classmethod
    def get_all_category(cls):
        return cls.__db


# a = Category()
# a.save("shoes")
# a.save("cloth")
# a.save("shoes")
# a.delete(1)

# print(a.get_all_category())
