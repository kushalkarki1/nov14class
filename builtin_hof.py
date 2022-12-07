# map, filter

# def total(a, b):
#     return a+b
# lambda a, b:a+b
# total = lambda a, b:a+b
# print(total(10, 15))

# map(func, iterable_object)

def increment_by_one(n):
    return n + 1

a = [1, 2, 3, 4, 5, 6, 7, 8]
out = map(lambda n:n+1, a)
# print(list(out))

names = ["ram", "shyam", "sita", "hari", "gita"]
out = map(lambda name:name.capitalize(), names)
# print(list(out))

# filter
# filter(func, iterable_object)
# func should return boolean value
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# out = [2, 4, 6, 8, 10]

def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    return num % 2 == 0

# out = filter(is_even, a)
out = filter(lambda num:num % 2 == 0, a)
# print(list(out))

emails = ["1@gmail.com", "2@gmail.com", "3@yahoo.com",
        "4@gmail.com", "5@yahoo.com", "6@outlook.com"]

# out = []
d = [17, 20, 25, 30]
c = ["17", "20", "25", "30"]
b = "12d57d54d90"
a = "457d89e36"

# d = [17, 20, 25, 30]
# total = 0
# for i in d:
#     total = total + i
# print(total)
# print(sum(d))

# c = ["17", "20", "25", "30"]
# total = 0
# for i in c:
#     total = total + int(i)

# print(total)
# print(sum(map(int, c)))
# b = "12d57d54d90"
# v = b.split("d")

a = "457d89e36"
total = 0
for i in a:
    if i.isnumeric():
        total = total + int(i)

print(total)

# print(sum(map(int,filter(lambda v:v.isnumeric(), a))))

# define a function which returns a list of
# prime numbers between provided range

def get_prime_numbers(start, stop):
    # 1, 100
    # return prime numbers between 1 to 100
    pass