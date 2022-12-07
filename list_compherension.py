# a = []
# for i in range(2, 20, 2):
#     a.append(i)

# print(a)
# a = [i for i in range(2, 20, 2)]
# print(a)

b = [i for i in range(1, 10) if i % 2 == 0]
print(b)

emails = ["1@gmail.com", "2@gmail.com", "3@yahoo.com",
        "4@gmail.com", "5@outlook.com", "6@yahoo.com",]

print([i for i in emails if i.endswith("@gmail.com")])