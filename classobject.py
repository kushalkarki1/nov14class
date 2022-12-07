# 1. Class and Object
# 2. Inheritance
# 3. Abstraction
# 4. Polymorphism

# Noun -> object
# adjective -> property, characteristics
# verb -> method, function, action

class Student:

    college = "ABC College" # class or static variable

    # Initializer function
    def __init__(self, _id, roll_no, name, gender):
        self._id = _id
        self.roll_number = roll_no
        self.name = name
        self.gender = gender
        self.total_attendance = 0

    def view_attendance(self):
        return f"Total attendance of {self.name} is {self.total_attendance}."

    def __str__(self):
        return f"{self.roll_number}.{self.name}"

    def __repr__(self):
        return f"{self.name}"

# s = Student(1, 1, "Ram", "Male")
# print(s)
# print(s.__dict__)
# print(f"Name: {s.name}")
# print(f"Roll number: {s.roll_number}")
# print(s.view_attendance())
# s2 = Student(2, 2, "Sita", "Female")
# print(s2.view_attendance())


################ STUDENT RECORDS #######################
# students = []
# for i in range(1, 6):
#     roll_n = input("Enter roll number: ")
#     name = input("Enter name: ")
#     gender = input("Enter gender: ")
#     s = Student(i, roll_n, name, gender)
#     students.append(s)

# print(students)
# for student in students:
#     print(f"Name: {student.name}")
#     print(f"Roll number: {student.roll_number}")
    # print(student.view_attendance())
#     print("-"*50)

# Staff => _id, name, contact, designation

class ProductPriceError(Exception):
    pass

class Product:

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ProductPriceError("Price can not be smaller than zero")
        self.__price = price

# tshirt = Product("T-Shirt", "123", 500)
# print(tshirt.__dict__)
# try:
#     tshirt.price = -200
# except ProductPriceError as err:
#     print(err)
# # tshirt.price = -200
# print(tshirt.__dict__)


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def difference(self):
        return self.num1 - self.num2

    def product(self):
        return self.num1 * self.num2

    @staticmethod
    def sqrt(num):
        return num**0.5

c = Calculator(20, 10)
print(c.add())
print(c.difference())
print(c.product())
print(Calculator.sqrt(25))