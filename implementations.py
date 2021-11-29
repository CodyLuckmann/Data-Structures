# Tuple to store all months in a year

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print(months[2])

# Set to store fruits

fruits = {"Apple", "Orange", "Banana", "Blueberry", "Strawberry"}
fruits.update(["Cherry", "Blackberry", "Carrot", "Cucumber"])

for item in fruits:
    print(item)

# Dictionary to store User Profile

person = {"firstName": "Joe",
          "lastName": "Johnson",
          "emailAddress": "joej@msn.com",
          "phoneNumber": "414-432-4356"}

for item in person:
    print(person.get(item))
