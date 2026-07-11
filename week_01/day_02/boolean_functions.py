# Creating Boolean Variables
is_learning = True
is_completed = False
print(is_learning)
print(is_completed)
# Creating Boolean Expressions
a = 10 > 5
b = 10 == 5
c = 10 < 5
print(a, b, c)

# Using if-else 
A = 200
B = 500
if A > B:
    print(A, "is greater than", B)
else:
    print(B, "is greater than", A)
# Using bool() Function
print(bool("Hello"))
print(bool(15))
print(bool(False))
print(bool("False"))
print(bool(None))
print(bool(0))
print(bool({}))
print(bool(()))
print(bool([]))

# Working with boolean functions
# checking whether the number is even/odd
def is_even(number):
    return number % 2 == 0
print(is_even(10))
print(is_even(340567345294214))
print(is_even(51))
print(is_even(4567893))
number = 24
if is_even(number):
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

# checking whether the person is adult/not
def is_adult(age):
    return age >= 18
print(is_adult(24))
print(is_adult(21))
print(is_adult(13))

age = 13
if is_adult(age):
    print("adult")
else:
    print("not an adult")

# checking whether the email is valid/not with help of '@'
def is_valid_email(email):
    return '@' in email
print(is_valid_email('bhavana@gmail.com'))
print(is_valid_email('bhavanagmail.com'))
email = "bhavanagmail.com"
if is_valid_email(email):
    print(f"{email} is a valid email")
else:
    print(f"{email} is not a valid email")

# checking whether the role has permission
def has_permission(role):
    return role in ["Developer", "Engineer"]
print(has_permission("Developer"))
print(has_permission("employee"))
print(has_permission("engineer"))

role = "guest"
if has_permission(role):
    print(f"{role} has permission")
else:
    print(f"{role} doesn't have permission")

# Using isinstance() 
name = "Bhavana"
age = 22
CGPA = 84.32
is_passed = True
print(isinstance(name, str))
print(isinstance(age, int))
print(isinstance(CGPA, float))
print(isinstance(is_passed, str))
