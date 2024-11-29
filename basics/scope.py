# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.


# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()

# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

# Example
# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.

# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)



# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())