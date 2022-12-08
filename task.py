heros=['spider man','thor','hulk','iron man', 'captain america']

"""
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther'
after 'hulk', so remove it from the list first and
then add it after 'hulk'
4. Now you don't like thor and hulk because
they get angry easily :)
    So you want to remove thor and hulk
    from list and replace them with
    doctor strange (because he is cool).
    Do that with one line of code.

5. Sort the heros list in alphabetical order.
"""

# take user input 15 times in int
# main, even, odd, duplicate
# main, append all user input
# even, append all even numbers
# odd, append all odd numbers
# duplicate, append all exisiting numbers

main = []
even = []
odd = []
duplicate = []

# for i in range(15):
#     num = int(input("Enter number: "))
#     if num in main:
#         duplicate.append(num)
#     else:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     main.append(num)

# print(f"Main list: {main}")
# print(f"Even list: {even}")
# print(f"Odd list: {odd}")
# print(f"Duplicate list: {duplicate}")


a = {
    "properties":{
        "profile":{
            "name": "ram",
            "education":[
                {"college": "abc", "year": 2018},
                {"college": "xyz", "year": 2020},
            ]
        },
        "followers": 10000,
        "following": 100,
    }
}

# Name: Ram
# Followers: 10000
# Following: 100
# Education(2018): ABC
# Education(2020): XYZ

name = a.get("properties").get("profile").get("name")
followers = a.get("properties").get("followers")
following = a.get("properties").get("following")
# print(f"Name: {name.capitalize()}")
# print(f"Followers: {followers}")
# print(f"Following: {following}")
educations = a.get("properties").get("profile").get("education")
for education in educations:
    college = education.get("college")
    year = education.get("year")
    # print(f"Education({year}): {college.upper()}")

######################################################################
oil_prices = [
    {
        "oil_type": "petrol",
        "prices":[
            {"year": 2018, "price": 100},
            {"year": 2019, "price": 150},
            {"year": 2020, "price": 180},
        ]
    },
    {
        "oil_type": "diesel",
        "prices":[
            {"year": 2018, "price": 80},
            {"year": 2019, "price": 100},
            {"year": 2020, "price": 160},
        ]
    }
]

# --------------------------------
# Oil Type: Petrol
# Price(2018):
# Price(2019):
# Price(2020):
# Avergae Price(2018-2020):
# --------------------------------
# Oli Type: Diesel
# Price(2018):
# Price(2019):
# Price(2020):
# Average Price(2018-2020):
# -----------------------------------

print("-"*50)
for oil in oil_prices:
    print(f"Oil Type: {oil.get('oil_type').capitalize()}")
    prices = oil.get("prices")
    total_price = 0
    for price in prices:
        year = price.get('year')
        p = price.get('price')
        total_price = total_price + p
        print(f"Price({year}): Rs.{p}")
    avg_price = round((total_price / len(prices)), 2)
    print(f"Average Price: {avg_price}")
    print("-"*50)

students_score = [
    {"name": "Ram", "score": 80},
    {"name": "Sita", "score": 100},
    {"name": "Abc", "score": 35},
    {"name": "xyz", "score": 40},
    {"name": "john", "score": 37},
    {"name": "Shyam", "score": 90},
    {"name": "hari", "score": 36},
]
out = []
for i in students_score:
    score = i.get("score")
    if score >= 40:
        out.append(i)

# print(out)

output = list(filter(lambda i:i.get("score") >= 40, students_score))
# print(output)


colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
removelist = ["yellow", "red"]
#remove these colors from remove list

colors = ["yellow", "red", "greeen", "blue", "yellow", "orange", "red"]
# take user input two times which color to be removed.
# and remove those colors