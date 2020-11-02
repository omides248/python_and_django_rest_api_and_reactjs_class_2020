# def hello(function):
#     print("hello omid")
#     function()


# def hi():
#     print("hi nastaran")


# hello(hi)

is_login = False


def my_decorator1(function):
    def wrapper():
        if is_login:
            print("Before run function")
            function()
            print("After run function")

    return wrapper


# @my_decorator1
# def hello():
#     print("hello")
#
#
# hello()

# def hello():
#     print("hello")


# hello_msg = my_decorator(hello)
# hello_msg()

print("----------------------------------")


def my_decorator2(function):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        if is_login:
            print("Before run function")
            function(*args, **kwargs)
            print("After run function")

    return wrapper


@my_decorator2
def hello(username, password):
    print("hello")


# hello("omid", "1234")

print("-----------------------------------------------------")


def my_decorator3(argument):
    print(argument)

    def my_decorate(function):
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            if is_login:
                print("Before run function")
                function(*args, **kwargs)
                print("After run function")

        return wrapper

    return my_decorate


@my_decorator3("sdafjksdaf")
def hello(username, password):
    print("hello")


hello("a", "b")
