my_dict = {
    "phone_number": "09331114355",
    "first_name": "omid 1",
    "last_name": "omid 2",
    "password": "1234",
    "confirm_password": "1234"
}
print(my_dict)
confirm_password = my_dict.pop("confirm_password")
print(confirm_password)
print(my_dict)