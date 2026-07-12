# Learning Python Operators
# Arithmetic operators
X = 14
Y = 2

print("Addition:",X + Y)
print("Subtraction:",X - Y)
print("Multiplication:",X * Y)
print("Division:",X / Y)
print("Remainder:",X % Y) 
print("Power:",X ** Y)
print("Floor Division:",X // Y) 

# Assignment operators
score = 12
print("Score: ",score)

score += 2
print("Score: ",score)

score -= 3
print("Score: ",score)

score *= 2
print("Score: ", score)

score /= 2
print("Score: ", score)

score //= 2
print("Score: ", score)

score %= 3
print("Score: ", score)

score **= 2
print("Score: ", score)

# Ternary Operators

Age = 23
check = "Adult" if Age >= 18 else "Minor"
print(check)

number = 3456
result = "Even" if number % 2 == 0 else "Odd"
print(result)

marks = 42
qualified = "Pass" if marks >= 50 else "Fail"
print(qualified)

# Comparison operators
x = 12
y = 15

print("Equal:", x == y)
print("Not equal to:", x!=y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)

age = 45
print(20 <= age <= 75)

# Logical operators
age = 30
has_ID = True
print("Output:", age >= 20 and has_ID)

is_member = True
has_coupon = False
if is_member or has_coupon:
    print("Discount Available")
else:
    print("No Discount")

print("original value:",has_coupon)
print("after not value:",not has_coupon)

# Identity operators
list1 = ["apple", "banana"]
list2 = ["apple", "banana"]
list3 = list1

print("Same values:", list1==list2)
print("Same objects:", list1 is list2)
print("list1 and list3 are same objects:", list1 is list3)
print("Different Objects:", list1 is not list2)

value = None
print("Value is none:", value is None)
print("Value is not none:", value is not None)

if value is not None:
    print("allowed")
else:
    print("not allowed")

# Membership operators
fruits = ["banana", "apple", "cherry"]
print("banana" in fruits)
print("mango" in fruits)
print("mango" not in fruits)

skills = {"Python", "git", "SQL"}

print("has python skills:", "Python" in skills)
print("has java skills:", "java" in skills)
print("doesn't have java skills:", "java" not in skills)

student = {
    "name": "bhavana",
    "age": 22,
    "city": "bengaluru"
}

print("name as key:", "name" in student)
print("bhavana as value:", "bhavana" in student)
print("bhavana as value:", "bhavana" in student.values())

# operator precedence
print("without parenthesis:", 100 + 5 * 3)
print("With parenthesis:", (100 + 5) * 3)
print("left to right:", 4 + 6 - 10 + 8)
print("exponentiation:", 2 ** 3 ** 2)
print("exponentiation with parenthesis:", (2 ** 3)** 2)

AGE = 22
has_id = True
print("comparison and logical:", AGE >= 18 and has_id)

print("and before or:", True or False and True)
print("parentheses changed the result:",(True or False) and False)




