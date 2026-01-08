def flexible(*args, **kwargs):
    print(f" Arguments which are tuple:{args}")
    print(f" Keyword Arguments which are dict:{kwargs}")


flexible(1, 2, 3, name="ajmal")

