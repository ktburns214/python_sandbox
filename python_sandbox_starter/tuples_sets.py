# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create tuple
fruits = ("apples", "oranges", "grapes")

# create tuple using a constructor
fruits2 = tuple(("apples", "oranges", "grapes"))
print(fruits, fruits2)

# remember to leave trailing comma when only have one value
fruits3 = ("apples", )
print(fruits3, type(fruits3))

# get a value from a tuple
print(fruits[1])

# cannot change a value--will get an error

# delete--then becomes undefined
del fruits2

# length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {"apples", "oranges", "mangos"}

# check in in set--returns either true or false
print("apples" in fruits_set)

# add to set
fruits_set.add("grapes")
print(fruits_set)

# remove
fruits_set.remove("mangos")
print(fruits_set)

# clear set entirely--then returns empty set
fruits_set.clear()

# delete--then becomes undefined
del fruits_set
