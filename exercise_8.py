def multiplier(n):
    def multiply(x):
        return x*n
    return multiply


times3 = multiplier(3)
time5 = multiplier(5)

print(times3(10))
print(time5(10))
