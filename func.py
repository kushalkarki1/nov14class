# def func():
#     print("welcome")
#     print("bye bye")
# print()

# def welcome():
#     print("Welcome students")

# welcome() # function execution
# welcome # call by reference

def sum_of_two_numbers(num1, num2):
    total = num1 + num2
    return total

# a = int(input())
# b = int(input())
total_sum = sum_of_two_numbers(10, 15)
# print(total_sum)
# arguments

# int a = 5;

def profile(name, address, contact):
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Contact: {contact}")

# profile("Ram", "Ktm", "0987654321") # ->positional argument
# print("---------------------------------")
# profile("Ram", "0987654321", "Ktm")

# print("---------------------------------")
# print("---------------------------------")
# profile(name="Ram", address="Ktm", contact="09876543")
# print("---------------------------------")
# profile(name="Ram", contact="09876543", address="Ktm",)
# keyword argument


def total_sum(num1, num2):
    total = num1 + num2
    print(f"Total: {total}")

def total_sum_two(num1, num2):
    total = num1 + num2
    return total

# b = total_sum(10, 15)
# print(f"b: {b}")
a = total_sum_two(10, 25)
# print(f"a: {a}")


# *args, **kwargs

def example(*args):
    print(args)

# example(1, 2, 3, 4, 5)

def example2(**kwargs):
    print(kwargs)

# example2(name="Ram", contact="087654321", nickname="Ra")

def mix_function(*args, **kwargs):
    # print(args)
    for i in args:
        print(i)
    print(kwargs.get("name"))

# mix_function(1, 2, 3, name="Ram", nickname="Ra")

def multiple_of_num(num1, factor=5):
    return num1 * factor

print(multiple_of_num(10))