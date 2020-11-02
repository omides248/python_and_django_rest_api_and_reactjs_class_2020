def hello(*args, **kwargs):
    print(args, kwargs)
    # a = args[0]
    # b = args[1]
    # c = args[2]
    a, b, c = args
    print(a, b, c)


hello(1, 2, 3, a=22, b=33)
