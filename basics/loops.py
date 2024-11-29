# Python Loops
# Python has two primitive loop commands:


# while loops
# for loops



# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other 
# object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:


for x in "banana":
  print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
# and ends at a specified number.

for x in range(6):
  print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
  print(x)
else:
  print("Finally finished!")


# Nested Loops
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    
# If you want to iterate over the list with both the index and the value, you should use the enumerate() function
fruits = ["apple", "banana", "cherry"]
for index, x in enumerate(fruits):
  print(index)
  if x == "banana":
    continue
  print(x)
