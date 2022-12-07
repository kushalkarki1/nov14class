# exception handling

# try:
#     # code
# except Exception: # catch specific error or exception
#     # code
# except Exception: # catch specific error or exception
#     # code
# else:
#     #code
# finally:
#     # code


# take two user input, and, print their sum

try:
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    print(a + b)
    # print(c)
except ValueError:
    print("can not convert to integer")
except NameError:
    print("Something is not defined")
finally:
    print("code is executed.")

name = input("Enter name: ")
print(name)