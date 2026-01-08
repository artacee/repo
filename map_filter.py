adds = lambda x, y: x + y

print(adds(2, 4))

nums = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, nums))

even = list(filter(lambda x: x%2 == 0, nums))

print(squared, even)
