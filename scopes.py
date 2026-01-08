count = 8 


def addone(x: int):
    global count
    count += 1
    return count


print(addone(1))
# so here we use global to take the variable count outside the function

# nonlocal keyword used to refer to the outer function variable

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

#prints x , becuase we overwrote the parent x using nonlocal


