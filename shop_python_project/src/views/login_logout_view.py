from src.models.user import User
from src.session.session import Session


class LoginLogoutView:

    @classmethod
    def login(cls):

        """ Get user info of terminal """
        fields = ("username", "password")
        username, password = list(input(f"{field} :") for field in fields)
        if not username and password:
            print(f"username: {username}, password: {password} is empty")

        """ Check user exists in database """
        user = User.get_user(username)
        if user:
            if user.get("password", "") == password:

                if not Session.exists_with_username(username):
                    """ User is valid and add user to session """
                    if Session.save(username, user.get("role")):
                        print("User successfully login")
                        print(Session.get_first_session())
                        return

        print("User not found or username and password is incorrect or already login(logout for login another user)")

    @classmethod
    def logout(cls):
        pass


