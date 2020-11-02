import itertools

from tutorial.decorators import my_decorator2


class Category:
    __db = [{"id": "1", "name": "shoes"}, {"id": "2", "name": "cloth"}]
    __id = itertools.count(1)

    @my_decorator2
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

    @classmethod
    def create_csv(cls):
        import datetime
        import random
        import csv
        file = f"{datetime.datetime.now().timestamp()}-{random.randint(1000, 9999)}.csv"
        with open(file, "w", encoding="utf-8-sig", newline="") as f:
            fieldnames = ["name"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for ctg in cls.__db:
                name = ctg.get("name")
                c = {"name": name}
                writer.writerow(c)


# a = Category()
# a.save("shoes")
# a.save("cloth")
# a.save("shoes")
# a.delete(1)

# print(a.get_all_category())

# Category.create_csv()
Category.save("shoes")
Category.save("shoes")