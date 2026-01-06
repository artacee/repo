my = [1, 2, 3, 4]

if my:
    print("hi")

# here we can see that by default it is considered true to be the case this is called truthy

#in python everything is true except empty things

# is vs ==

a = [1, 3, 5]
b = [1, 3, 5]

print(a is b)
print(a == b)

# use of and or
input_name = ""
username = input_name or "guest"
# if inputnmae is falsy that is empty it defaults to guest
