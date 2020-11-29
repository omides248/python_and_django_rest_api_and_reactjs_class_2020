import re
from kavenegar import *

prefix_phone_numbers = {
    "irancell": ["930", "933"],
    "hamrah_aval": ["915"]
}

API_KEY = ""

allow_operators = ["irancell"]


def valid_phone_number(phone_number: str = None) -> bool:
    return False if not phone_number or len(re.findall(r"^(?:0|\+98)\d{10}$", phone_number)) == 0 else True


def get_operator_name(phone_number: str = None) -> (str, str):
    if not phone_number:
        return "", "Phone_number not found"

    if not valid_phone_number(phone_number):
        return "", "phone number is not valid"

    prefix_num = phone_number[-10: -7]  # [-10, -7)
    for operator_name, prefix_num_list in prefix_phone_numbers.items():
        if prefix_num in prefix_num_list:
            return operator_name, ""

    return "", "operator not found"


def send_sms(phone_number: str = None, message: str = None) -> (str, str):
    if not phone_number:
        return "", "Phone_number not found"

    if not message:
        return "", "message is empty"

    if not valid_phone_number(phone_number):
        return "", "phone number is not valid"

    try:
        api = KavenegarAPI(API_KEY)
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': message,
        }
        response = api.sms_send(params)
        return phone_number, str(response)
    except APIException as e:
        return "", str(e)
    except HTTPException as e:
        return "", str(e)


def send_sms_multi_user(phone_numbers: list = None, message: str = None) -> (str, str):
    if not phone_numbers:
        return "", "phone_numbers is empty"

    if not message:
        return "", "message is empty"

    phone_numbers_allow = []

    for phone_number in phone_numbers:
        opn, _ = get_operator_name(phone_number)
        if valid_phone_number(phone_number) and opn in allow_operators:
            phone_numbers_allow.append(phone_number)

    if len(phone_numbers_allow) == 0:
        return "", "Isn't allow All phone numbers"

    phone_numbers_allow_str = ",".join(phone_numbers_allow)

    send_sms(phone_numbers_allow_str)


phone_number = "09331112233"
print(valid_phone_number(phone_number))

operator_name, err = get_operator_name(phone_number)
if not err:
    print(operator_name)
else:
    print(err)

a = ["09331112244", "09331112233"]
res, err = send_sms_multi_user(a, "my message for users")
print(res, err)
