# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Katie"
age = 29

# concatenate
print("Hello, my name is " + name + " and I am " + str(age))

# String Formatting
# positional arguments
print("My name is {name} and I am {age}".format(name=name, age=age))

# F-strings
print(f"Hello, my name is {name} and I am {age}")

# String Methods
s = "hello world"

# capitalize string
print(s.capitalize())

# make all uppercase
print(s.upper())

# make all lowercase
print(s.lower())

# swapcase
print(s.swapcase())

# get length
print(len(s))

# replace
print(s.replace("world", "everyone"))

# count--counts occurance of a character
sub = "h"
print(s.count(sub))

# starts with--outputs true or false value
print(s.startswith("hello"))

# ends with--outputs true or false value
print(s.endswith("d"))

# slpit into list
print(s.split())

# find position of a character
print(s.find("r"))

# is all alphanumeric--true or false, includes spaces
print(s.isalnum())

# is all alphabetic--true or false, includes spaces
print(s.isalpha())

# is all numeric--true or false
print(s.isnumeric())
