class Manager:

    def all(self):
        return [1, 2, 3, 4]


class Model(Manager):
    objects = Manager()


class CategoryManager(Manager):

    def active(self):
        return [2, 3, 4, 5]


class Category(Model):
    objects = CategoryManager()
    active_objects = CategoryManager()


print(Category.objects.all())
print(Category.active_objects.all())
print(Category.objects.active())
print(Category.active_objects.active())
