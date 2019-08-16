# A Dictionary is a collection which is unordered, changeable, and indexed. No duplicate members.
# similar to object literal in JS

# create dict
person = {
    "first_name": "Katie",
    "last_name": "Burns",
    "age": 21
}
print(person, type(person))

# create dict using a constructor
person2 = dict(first_name="Sarah", last_name="Williams")
print(person2, type(person2))

# get a value
print(person["first_name"])
# get method
print(person.get("last_name"))

# add key value
person["phone"] = "867-5309"
print(person)

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy a dict--similar to how spread operator works in JS
person3 = person.copy()
person3["city"] = "Chicago"
print(person3)

# remove an item
del(person["age"])
print(person)
# remove an item using pop
person.pop("phone")
print(person)

# clear--returns empty dict
person.clear()
print(person)

# get length
print(len(person2))

# list of dict
people = [
    {"name": "Martha", "age": 30},
    {"name": "John", "age": 100}
]
print(people)

# get a certain value
print(people[1]["name"])
