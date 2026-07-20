# Getting started with strings
message = """ Hello Python!', Learning a programming language successfully within short period is not an easy task"""
print(message)
my_message = "Bobby's World"
print(my_message)
# len() function example
print(len(my_message))
# Accessing the individual characters of a string using index
print(my_message[0]) 
print(my_message[12])
# Accessing the range of characters
print(my_message[:7])
print(my_message[:])
print(my_message[1:])
print(my_message[1:5])
# String methods
print(my_message.lower())
print(my_message.upper())
print(my_message.count("Bobby"))
print(my_message.find("World"))
print(my_message.find("Bhavana"))
print(my_message.replace("World", "Home"))
# String Concatenation
greeting = "Hello"
name = "Bhavana"
print(greeting + ", " + name)
# Formatted strings
print(f"{greeting}, {name}")
print(dir(name))
print(help(str.lower))
