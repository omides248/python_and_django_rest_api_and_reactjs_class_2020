from src.decorators.user_decorators import check_permissions
from src.enums import EnumRole
from src.models.user import User


class RegisterView:

    @classmethod
    @check_permissions(admin_access=True)
    def create_employee(cls) -> (bool, str):

        fields = ("username", "first_name", "last_name", "password")
        username, first_name, last_name, password = list(input(f"{field} :") for field in fields)

        if not User.exists_with_username(username):
            User.save(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                role=EnumRole.EMPLOYEE
            )
            return True, ""
        else:
            return False, f"This username: {username} already exists"

    @classmethod
    def create_customer(cls) -> (bool, str):

        fields = ("username", "first_name", "last_name", "password")
        username, first_name, last_name, password = list(input(f"{field} :") for field in fields)

        if not User.exists_with_username(username):
            User.save(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                role=EnumRole.CUSTOMER
            )
            return True, ""
        else:
            return False, f"This username: {username} already exists"
