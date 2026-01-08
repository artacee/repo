import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)

        end = time.time()
        print(f"FUNCTION TOOK {end - start} seconds")
        return result
    return wrapper

@timer
def heavy():
    sum([i**2 for i in range(1000000)])

heavy()

