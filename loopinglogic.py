# enumerate
Interns = ["Rani", "Chikku", "Ajmal"]

for index, name in enumerate(Interns):
    print(index, name)
# zip
Name = ["Aju", "Gaju", "kaju"]
Age = [21, 22]

for kiladi, kiladi_age in zip(Name, Age):
    print(f"{kiladi} is {kiladi_age}")

# list comprehensions

numbers = [1, 2, 3, 4, 5]

squares = [n**2 for n in numbers if n%2 == 0]
odd_squares = [n**2 for n in numbers if n%2 != 0]

oneplus = [ n+1 for n in numbers]

print(squares, odd_squares, oneplus)
