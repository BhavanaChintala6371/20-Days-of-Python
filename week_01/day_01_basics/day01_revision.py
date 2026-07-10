# Day 01 Revision: Python Basics, Variables, Data Types, Numbers, Casting, and Strings
# Output and comments
print("Hello Python!")
print("I am learning Python")
print("10 + 20")
print(10 + 20)
# Variables
name = "Bhavana Chintala"
city = "Hyderabad"
goal = "Python job preparation"
print("Name:", name)
print("City:", city)
print("Goal:", goal)
# Variable names and multiple assignment
lead_count, reply_count, meeting_count = 100, 12, 3
print("Lead count:", lead_count)
print("Reply count:", reply_count)
print("Meeting count:", meeting_count)
status1 = status2 = status3 = "Pending"
print(status1)
print(status2)
print(status3)
# Data types
reply_rate = reply_count / lead_count * 100
print(type(name))
print(type(lead_count))
print(type(reply_rate))
# Numbers
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
# Casting
x = "100"
y = 50
print(int(x) + y)
a = int(2.8)
b = float(3)
c = str(25)
print(a)
print(b)
print(c)
# Strings
full_name = " Bhavana Chintala "
email = "BHAVANA@GMAIL.COM"
clean_name = full_name.strip().title()
clean_email = email.lower()
print(clean_name)
print(clean_email)
print(clean_name[0])
print(clean_name[-1])
print(len(clean_name))
# Slicing
text = "Python Programming"
print(text[0:6])
print(text[7:])
# Check string
print("@gmail.com" in clean_email)
print("Java" not in text)
# Replace and split
message = "I am learning Java"
message = message.replace("Java", "Python")
print(message)
data = "apple,banana,cherry"
print(data.split(","))
# F-string formatting
print(f"My name is {clean_name}. I am from {city}.")
print(f"Out of {lead_count} leads, {reply_count} replied.")
print(f"Reply rate: {reply_rate:.2f}%")
# Escape characters
print("She said \"Python is easy\"")
print("Name: Bhavana\nGoal: Learn Python\nDay: 1")
print("Name:\tBhavana")