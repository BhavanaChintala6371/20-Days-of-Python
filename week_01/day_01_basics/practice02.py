print("Hi, Python!")
print(10 + 20)
print(40/20)
print(20 * 2)
print("Bhavana")

# this is my first python program
print("I am in LOVE with python")
name = "Bhavana Chintala"
print("My name is", name)
age = 22
print("My age is", age)
city = "Bengaluru"
print("I am from", city)
goal = "Getting a job in python within the next 30 days"
print("My goal is: ",goal)

# Valid Varialble Names
name = "Bhavana"
_age = 22
rank1 = "Above Average"
interested_in = "python relevant roles"

print(name,_age, rank1, interested_in)

# Assigning multiple valuesto multiple variables
name, degree, interest, age = "Bhavana", "B.Tech", "Python", 22

print(name, degree, interest, age)

#Assigning same value to multiple variables
Bhavana = Rama = Sita = "B.Tech"

print(Bhavana, Rama, Sita)

# printing multiple variables in a single print statement separated by comma's
# comma will automatically add a space between the variables while printing
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

""" printing multiple variables in a single print statement using '+' operator
Remember: '+' operator will not add a space between the variables while printing
we have to add a space manually """
x = "Python "
y = "is "
z = "awesome"
print(x+y+z)

name = "Bhavana"
age = 22
major = "B.Tech"
CGPA = 8.43
is_interested_in_python = True
print(name, age, major, CGPA, is_interested_in_python)
# Using type() function to check the data type of the variables
print(type(name), type(age), type(major), type(CGPA), type(is_interested_in_python))

x = 3 + 4j
print(x, type(x))

a = 20/2
print(a)
print(CGPA, type(CGPA))
new_name =int(CGPA)
print(new_name, type(new_name))
new_age = str(age)
print(new_age,type(new_age))

text1 = 'python is my "favorite" programming language'
text2 = "Iam getting good at python 'everyday'"
text3 = '''I am so happy
as i am progressing
i am excited for the opportunities that are coming on my way '''
text4 = """I would like to thank few people
who have been a great support to me in this journey """
print(text1)
print(text2)
print(text3)
print(text4)