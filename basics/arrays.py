# Python Arrays
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.


# Arrays
# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, 
# like the NumPy library.

# Arrays are used to store multiple values in one single variable:


# ExampleGet your own Python Server
# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]

# What is an Array?
# An array is a special variable, which can hold more than one value at a time.

# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

# The solution is an array!

# An array can hold many values under a single name, and you can access the values by referring to an index number.




# Access the Elements of an Array
# You refer to an array element by referring to the index number.

# Get the value of the first array item:

x = cars[0]


# Modify the value of the first array item:
cars[0] = "Toyota"



# Return the number of elements in the cars array:
x = len(cars)

for x in cars:
  print(x)


# Print each item in the cars array:

for x in cars:
  print(x)

# Add one more element to the cars array:
cars.append("Honda")

# Delete the element that has the value "Volvo":
cars.remove("Volvo")


# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list