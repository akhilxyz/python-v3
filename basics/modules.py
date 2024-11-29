# Python Modules

# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.


# Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)


# Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")


# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

# Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)