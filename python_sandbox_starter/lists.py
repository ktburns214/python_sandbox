# A List is a collection which is ordered and changeable. Allows duplicate members.
# lists in python are similar to arrays

# create list
numbers = [1, 2, 3, 4, 5]

fruits = ["apples", "oranges", "grapes", "strawberries"]

# create list using a constructor
numbers2 = list((6, 7, 8, 9))

print(numbers, numbers2)

# get a single value from list
print(fruits[1])

# get length
print(len(fruits))

# append to list
fruits.append("mangos")
print(fruits)

# remove from list
fruits.remove("grapes")
print(fruits)

# insert into position
fruits.insert(2, "raspberries")
print(fruits)

# change a value
fruits[0] = "blueberries"
print(fruits)

# remove with pop
fruits.pop(2)
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

# sort list alphabetically
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)
