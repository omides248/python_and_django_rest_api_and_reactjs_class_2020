from src.decorators.user_decorators import check_permissions
from src.models.category import Category


class CategoryView:

    @classmethod
    def show_all(cls):
        print(Category.get_all_categories())

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def add_category(cls):
        name = input("name: ")
        if Category.save(name):
            print(f"Successfully add category: {name}")
        else:
            print(f"This category exists with {name}")

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def update_category(cls):
        _id = input("id: ")
        name = input("name: ")
        if Category.update(_id, name):
            print(f"Successfully update category with id:{_id} name: {name}")
            return 1, 2
        else:
            print("Category not found for update")
            return 3, 4

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def delete_category(cls):
        _id = input("id: ")
        result, err = Category.delete(_id)
        if result:
            print(f"Successfully deleted category with _id: {_id}")
        else:
            print(err)
