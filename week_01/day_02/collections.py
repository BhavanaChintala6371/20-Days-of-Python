courses = ["Maths", "Physics", "Science"]
print(courses)
# Using len() to know the size of the list
print(len(courses))
# Accessing values using index and slicing 
print(courses[0])
print(courses[:1])
print(courses[1:])
print(courses[-3:])
print(courses[:-1]) 

courses.append("Art")
print(courses)

courses.insert(0,"Art")
print(courses)