# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django), as well as custom modules

# import a core python module (i.e. datetime)
import datetime
today = datetime.date.today()
print(today)

# import a certain piece of a core python module (i.e. time)
from time import time
timestamp = time()
print(timestamp)

# pip module (i.e. camelcase)
from camelcase import CamelCase 
c = CamelCase()
print(c.hump("hello world"))

# import custom module (i.e. validator.py)
import validator
from validator import validate_email

email = "test@test.com"
if validate_email(email):
    print("email is valid")
else:
    print("email is bad")
