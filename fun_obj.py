def shout(text: str):
    return text.upper()


def whisper(text: str):
    return text.lower()

def greet(func):
    greeting = func("hi hello")
    print(greeting)

greet(shout)
greet(whisper)



hi = print

hi("hello")
