data = "Value: 42; Price: 99.5 "

#qn need to extract the two numbers and add them together

new_data = [number.strip(";") for number in data.split()]

numbers = list(map(float, new_data[1::2]))
sums = sum(numbers)

print(sums)

