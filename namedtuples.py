from collections import namedtuple

user = namedtuple('User', ['id', 'name', 'age'])

u1 = user(1, "Alice", 30)

print(u1.name)
print(u1[1])
