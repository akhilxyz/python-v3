# F-Strings
# F-string allows you to format selected parts of a string.

# To specify a string as an f-string, simply put an f in front of the string literal, like this:

txt = f"The price is 49 dollars"
print(txt)


# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

# Example
# Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)


# A placeholder can also include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# Example
# Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


# You can also format a value directly without keeping it in a variable:

# Example
# Display the value 95 with 2 decimals:

txt = f"The price is {95:.2f} dollars"
print(txt)