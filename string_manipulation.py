# dir(str)
# help(str.capitalize)

a = 10
b = 20
total = a + b

print("The sum of ",a, "and", b, "is", total," .")
e = "The sum of {} and {} is {}".format(a, b, total)
# e = "The sum of ",a, "and", b, "is", total," ."
print(e)
abc = f"The sum of {a} and {b} is {total}."
print(abc)