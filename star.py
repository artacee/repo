s = input("Enter the number: ")
s = list(s)
a = 0
l = len(s)
for i in s:
    a += (int(i))**l
if a == s:
    print("armstrong")
else:
    print("not")


