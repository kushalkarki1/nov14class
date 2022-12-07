# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     inner()

# outer()


# def welcome(name):
#     print(f"Welcome {name}!")

# a = welcome
# print(f"Welcome: {welcome}")
# print(f"a: {a}")
# a("Shyam")


def increment(num):
    def increase_by(factor):
        return num + factor
    # value = increase_by(10)
    return increase_by

# a = increment(20)
# print(a(20))
# print(a(10))


def welcome(name):
    print(f"Welcome {name}")

def bye_bye(name):
    print(f"Bye bye {name}")

def greet_person(a): # a = welcome # higher order function
    a("Ram") # welcome("Ram")

# greet_person(bye_bye)

# higher order function (built in)
# decorator

def decorate_function(func):
    def wrapper():
        print("Called before.")
        func()
        print("Called after.")
    return wrapper

@decorate_function
def example():
    print("I am example.")

# d = decorate_function(example)
# d()
# example()
# print(example)

def smart_division(func):
    def wrapper(a, b):
        if b == 0:
            return "can not divide by zero."
        else:
            return func(a, b)
    return wrapper

@smart_division
def division(a, b):
    return a / b

print(division(10, 2))
print(division(10, 0))