# the hard way

def my_decorater(func):
    def wrapper():
        print("something")
        func()
        print("someething")
    return wrapper


def say_hello():
    print("hello")


say_hello = my_decorater(say_hello)

say_hello()

# using @


@my_decorater
def say_whee():
    print("weeeeee")


say_whee()
