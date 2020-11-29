from src.enums import EnumRole
from src.session.session import Session


def check_permissions(admin_access: bool = False, employee_access: bool = False,
                      customer_access: bool = False) -> object():
    def permissions(function):
        def wrapper(*args, **kwargs):

            if not Session.exists_with_username():
                print("Please login or register")

            if (Session.is_admin() and admin_access) or \
                    (Session.is_employee() and employee_access) or \
                    (Session.is_customer() and customer_access):

                function(*args, **kwargs)

            else:
                message = "This option access only "
                users = list()
                if admin_access:
                    users.append(f"\"{EnumRole.ADMIN}\"")
                if employee_access:
                    users.append(f"\"{EnumRole.EMPLOYEE}\"")
                if customer_access:
                    users.append(f"\"{EnumRole.CUSTOMER}\"")

                message += " and ".join(users)
                print(message)

        return wrapper

    return permissions
