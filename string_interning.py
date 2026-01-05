a = "hello"

b = "hello"

print( a is b )
print(id(a), id(b))

z = "hello world"

y = "hello world"
print( z is y)
print(id(z), id(y))

#usually not same but this compiler version shows as same
