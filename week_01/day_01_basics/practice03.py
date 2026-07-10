name = "Bhavana"
# Accessing the characters of a string using indexing
print(name[0])
print(name[1], name[-1], name[-7])
print(name[-0])

name = "Bhavana Chintala"
aim = "Getting a job in python ASAP"
# using len() function to get the length of the string
print(len(name))
# demonstration of len() function can't be used to get the no.of words in a string
print(len(aim))


sentence = "Python is a programming language"
# checking if a substring exists in a string using 'in' and 'not in'operators
# results in boolean values True or False
print("Python" in sentence)
print("Java" in sentence)
email = "bhavana.chintala@gmail.com"
print("@Gmail.com" not in email)
print("@gmail.com" in email)

name = "Python Programming"
print(name[:18]) # printing the whole string using slicing,start is empty means it will start from beginning 
print(name[0:]) # printing the whole string using slicing, end is empty means it will go till the end
print(name[1:10]) # printing the string from index 1 to 9
print(name[-11:]) # printing the string from index -11 to the end
print(name[:-1]) # printing the string from beginning to index -2

text = "I love Python programming "
print(text.lower()) # converting the string to lowercase
print(text.upper()) # converting the string to uppercase
print(text.strip()) # removing the Leading and trailing spaces from the string
print(text.replace("programming", "Applications")) # replacing a substring with another substring
print(text.split(" ")) # splitting the string into a list of substrings
print(text.capitalize()) # converting the first character to uppercase and the rest to lowercase
print(text.title()) # converting the first character of each word to uppercase and the rest to lowercase

first_name = "Bhavana"
last_name = "Chintala"
age = 22
# concatenating two strings using + operator
full_name = first_name + " " + last_name
print(full_name)
print(f"My name is {full_name} and I am {age} years old.") # use f-string for printing strings and numbers together
value = 3.14159
# formatting the float value to 2 decimal places using f-string
print(f"the value of pi is {value:.2f}")
interest = "\\ \tI am \"Interested\" in\n \'Python\' programming language"
print(interest) # Printing the string with escape characters

































































