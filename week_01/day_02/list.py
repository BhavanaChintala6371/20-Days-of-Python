# Creating List with same and different values
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30]
mixed = ["Bhavana", 25, True, 99.5]
print(len(fruits))
print(type(fruits))

# Accessing list items
fruits = ["custard", "mulberry", "guava", "apple", "orange", "banana","mango", "grapes"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-3])
print(fruits[-2])
print(fruits[-1])
print(fruits[4])
print(fruits[1:7])
print(fruits[:8])
print(fruits[0:])
print(fruits[-8:-1])
print("banana" in fruits)
print("papaya" not in fruits)
print("grapes" not in fruits)

# Changing the list items
fruits[0] = "banana"
print(fruits)
fruits[1:4] = ["blueberry", "cherry", "strawberry"]
print(fruits)
# replacing one item with multiple items
fruits[1:2] = ["watermelon", "jackfruit", "sapota"]
print(fruits)
# replacing multiple items with one item
fruits[4:8] = ["sapota"]
print(fruits)
# adding list items
# Inserting without replacing
fruits.insert(0, "jackfruit")
print(fruits)
fruits.append("pineapple")
print(fruits)
more_fruits = ["apple", "orange", "cherry"]
fruits.extend(more_fruits)
print(fruits)

# removing list items
# remove() deletes first matching value
fruits.remove("sapota")
print(fruits)
# pop() with index removes the item at index
fruits.pop(1)
print(fruits)
# pop() without index specification it removes last item
fruits.pop()
print(fruits)
# del to delete the item from specific index
del fruits[0]
print(fruits)

