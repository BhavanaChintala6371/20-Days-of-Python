# Day 02 Python Revision Notes

## Part 1 + Part 2: Booleans, Operators, Lists, Tuples, Sets, Frozenset, and Dictionaries

These notes reorganize the complete Day 02 material into a GitHub-friendly revision document. The content stays within the topics, examples, mistakes, practice problems, mini projects, interview questions, and checklist covered in the Day 02 PDF.

---

## Table of Contents

1. [Big Picture: Why These Topics Matter](#1-big-picture-why-these-topics-matter)
2. [Quick Comparison of Day 2 Concepts](#2-quick-comparison-of-day-2-concepts)
3. [Python Booleans](#3-python-booleans)
4. [`bool()` Function](#4-bool-function)
5. [Functions Returning Booleans](#5-functions-returning-booleans)
6. [`isinstance()`](#6-isinstance)
7. [Boolean Beginner Mistakes](#7-boolean-beginner-mistakes)
8. [Python Operators](#8-python-operators)
9. [Python Operator Groups](#9-python-operator-groups)
10. [Arithmetic Operators](#10-arithmetic-operators)
11. [Assignment Operators](#11-assignment-operators)
12. [Ternary Expression](#12-ternary-expression)
13. [Comparison Operators](#13-comparison-operators)
14. [Logical Operators](#14-logical-operators)
15. [Identity Operators](#15-identity-operators)
16. [Membership Operators](#16-membership-operators)
17. [Bitwise Operators](#17-bitwise-operators)
18. [Operator Precedence](#18-operator-precedence)
19. [Python Collections Overview](#19-python-collections-overview)
20. [Python Lists](#20-python-lists)
21. [Access List Items](#21-access-list-items)
22. [Change List Items](#22-change-list-items)
23. [Add List Items](#23-add-list-items)
24. [Remove List Items](#24-remove-list-items)
25. [Loop Lists](#25-loop-lists)
26. [List Comprehension](#26-list-comprehension)
27. [Sort Lists](#27-sort-lists)
28. [Copy Lists](#28-copy-lists)
29. [Join Lists](#29-join-lists)
30. [Important List Methods](#30-important-list-methods)
31. [Python Tuples](#31-python-tuples)
32. [Access Tuple Items](#32-access-tuple-items)
33. [Update Tuples](#33-update-tuples)
34. [Tuple Packing and Unpacking](#34-tuple-packing-and-unpacking)
35. [Loop Tuples](#35-loop-tuples)
36. [Join Tuples](#36-join-tuples)
37. [Tuple Methods](#37-tuple-methods)
38. [Python Sets](#38-python-sets)
39. [Access Set Items](#39-access-set-items)
40. [Add Set Items](#40-add-set-items)
41. [Remove Set Items](#41-remove-set-items)
42. [Loop Sets](#42-loop-sets)
43. [Join Sets and Set Operations](#43-join-sets-and-set-operations)
44. [Frozenset](#44-frozenset)
45. [Important Set Methods](#45-important-set-methods)
46. [Python Dictionaries](#46-python-dictionaries)
47. [Access Dictionary Items](#47-access-dictionary-items)
48. [Change Dictionary Items](#48-change-dictionary-items)
49. [Add Dictionary Items](#49-add-dictionary-items)
50. [Remove Dictionary Items](#50-remove-dictionary-items)
51. [Loop Dictionaries](#51-loop-dictionaries)
52. [Copy Dictionaries](#52-copy-dictionaries)
53. [Nested Dictionaries](#53-nested-dictionaries)
54. [Important Dictionary Methods](#54-important-dictionary-methods)
55. [Master Revision Code](#55-master-revision-code)
56. [Must-Remember Points](#56-must-remember-points)
57. [Beginner Mistakes to Avoid](#57-beginner-mistakes-to-avoid)
58. [Practice Problems](#58-practice-problems)
59. [Mini Projects](#59-mini-projects)
60. [Interview Questions](#60-interview-questions)
61. [Final Day 2 Checklist](#61-final-day-2-checklist)

---

# Foundation and Booleans

## 1. Big Picture: Why These Topics Matter

Until Day 1, the main focus was on individual values such as strings, integers, floats, Booleans, and `None`.

Day 2 moves into two major abilities:

- making decisions with Boolean logic and operators
- storing and organizing multiple values with collections

These topics are the foundation for:

- problem solving
- LeetCode and HackerRank exercises
- automation scripts
- backend and web applications
- data processing
- API responses
- database records
- real-world Python programs

### Core idea

- **Booleans** help a program make decisions.
- **Operators** calculate, compare, assign, and test values.
- **Lists, tuples, sets, frozensets, and dictionaries** store and organize multiple values.

```python
skills = ["Python", "SQL", "Git"]

if "Python" in skills:
    print("Python skill is available")
else:
    print("Python skill is missing")
```

### Key point

Day 2 should not be treated as syntax memorization. These topics explain how programs compare values, choose actions, group information, and process data.

---

## 2. Quick Comparison of Day 2 Concepts

| Concept | Main use |
|---|---|
| `bool` | Stores `True` or `False` |
| Operators | Perform operations on values |
| List | Ordered, changeable collection that allows duplicates |
| Tuple | Ordered, fixed collection that allows duplicates |
| Set | Unordered collection of unique values |
| Frozenset | Unordered, fixed collection of unique values |
| Dictionary | Ordered, changeable key-value data |

```python
is_learning = True
score = 10 + 5
fruits = ["apple", "banana"]
coordinates = (10, 20)
skills = {"Python", "SQL"}
fixed_skills = frozenset(["Python", "SQL"])
student = {"name": "Bhavana", "age": 25}
```

### Collection selection rule

Choose a collection based on:

- whether order matters
- whether the values should change
- whether duplicates should be allowed
- whether values need named keys

---

## 3. Python Booleans

A Boolean has only two possible values:

```python
True
False
```

Booleans represent answers such as:

- yes or no
- true or false
- valid or invalid
- available or unavailable

A **Boolean expression** returns `True` or `False`.

```python
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
```

A **condition** is a Boolean expression used to decide which code should run.

```python
age = 25

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Example

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
```

Output:

```text
b is not greater than a
```

### Key points

- Boolean values are written as `True` and `False`.
- Comparisons return Boolean values.
- `if...else` uses a Boolean condition to choose a code block.
- Python is case-sensitive: `true` and `false` are invalid names unless previously defined.

### Common mistakes

```python
# Wrong
is_learning = true

# Correct
is_learning = True
```

```python
# Wrong: assignment used where comparison is needed
if x = 10:
    print("Equal")

# Correct
if x == 10:
    print("Equal")
```

---

## 4. `bool()` Function

`bool()` checks whether a value behaves as `True` or `False`.

```python
bool(value)
```

### Truthy values

Most non-empty and non-zero values are truthy.

```python
print(bool("Python"))                 # True
print(bool(100))                      # True
print(bool(12.5))                     # True
print(bool([1, 2, 3]))                # True
print(bool(("apple", "banana")))     # True
print(bool({"name": "Bhavana"}))    # True
```

### Falsy values

The important falsy values are:

```python
False
None
0
""
[]
()
{}
set()
```

```python
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(()))     # False
print(bool({}))     # False
print(bool(set()))  # False
```

### Important beginner examples

```python
print(bool("False"))  # True
print(bool("0"))      # True
print(bool(" "))      # True
print(bool(""))       # False
```

Why?

- `"False"` is non-empty text.
- `"0"` is non-empty text.
- `" "` contains a space.
- only the final example is an empty string.

---

## 5. Functions Returning Booleans

A function can return a Boolean result so that the result can be reused.

```python
def is_adult(age):
    return age >= 18

print(is_adult(20))  # True
print(is_adult(15))  # False
```

Using the function inside a condition:

```python
def is_adult(age):
    return age >= 18

age = 21

if is_adult(age):
    print("Allowed")
else:
    print("Not allowed")
```

Useful Boolean-style function names include:

```python
is_valid_email(email)
is_even(number)
is_logged_in(user)
has_permission(role)
```

### Key point

Return a Boolean instead of printing inside every checking function when the result must be used later.

---

## 6. `isinstance()`

`isinstance()` checks whether a value belongs to a specified type. It returns `True` or `False`.

```python
isinstance(value, data_type)
```

```python
name = "Bhavana"
age = 25
price = 99.99
is_learning = True

print(isinstance(name, str))          # True
print(isinstance(age, int))           # True
print(isinstance(price, float))       # True
print(isinstance(is_learning, bool))  # True
```

### `type()` versus `isinstance()`

- `type(value)` shows the exact type.
- `isinstance(value, type)` checks membership in a type and returns a Boolean.

---

## 7. Boolean Beginner Mistakes

### Correct special values

```python
True
False
None
```

Not:

```python
true
false
none
```

### Assignment versus comparison

| Symbol | Meaning |
|---|---|
| `=` | Assign a value |
| `==` | Compare two values |

### Non-empty strings are truthy

```python
print(bool("False"))  # True
```

### Avoid unnecessary comparison with `True`

```python
is_valid = True

# Works, but unnecessary
if is_valid == True:
    print("Valid")

# Cleaner
if is_valid:
    print("Valid")
```

---

# Operators

## 8. Python Operators

An **operator** is a symbol or keyword that performs an action.

```python
10 + 5
```

- `+` is the operator.
- `10` and `5` are operands.

An **operand** is a value used by an operator.

An **expression** combines values, variables, and operators to produce a result.

```python
10 + 5
age >= 18
name == "Bhavana"
"Python" in skills
```

---

## 9. Python Operator Groups

Python operators are grouped by purpose:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators

```python
x = 10
y = 5

print(x + y)               # arithmetic
x += 2                     # assignment
print(x > y)               # comparison
print(x > 5 and y > 2)     # logical
print(x is y)              # identity
print("a" in "apple")      # membership
print(6 & 3)               # bitwise
```

Do not confuse:

- `and` with `&`
- `or` with `|`
- `==` with `is`
- `=` with `==`

---

## 10. Arithmetic Operators

| Operator | Name | Meaning | Example |
|---|---|---|---|
| `+` | Addition | Adds values | `x + y` |
| `-` | Subtraction | Subtracts values | `x - y` |
| `*` | Multiplication | Multiplies values | `x * y` |
| `/` | Division | Divides and returns a float | `x / y` |
| `%` | Modulus | Returns the remainder | `x % y` |
| `**` | Exponentiation | Raises to a power | `x ** y` |
| `//` | Floor division | Returns the floored quotient | `x // y` |

```python
x = 15
y = 4

print(x + y)   # 19
print(x - y)   # 11
print(x * y)   # 60
print(x / y)   # 3.75
print(x % y)   # 3
print(x ** y)  # 50625
print(x // y)  # 3
```

### `/` division

```python
print(10 / 5)  # 2.0
```

`/` returns a float, even when the result is mathematically a whole number.

### `//` floor division

```python
print(12 // 5)   # 2
print(-12 // 5)  # -3
```

Floor division rounds downward. It does not simply remove the decimal for negative values.

### `%` modulus

```python
print(15 % 4)  # 3
```

Checking even or odd:

```python
number = 10
print(number % 2 == 0)  # True
```

- `number % 2 == 0` means even.
- `number % 2 != 0` means odd.

### `**` exponentiation

```python
print(2 ** 3)  # 8
```

### Common mistakes

- `%` means remainder, not percentage.
- `/` returns a float.
- `//` performs floor division.

---

## 11. Assignment Operators

Assignment operators assign or update values.

| Operator | Example | Equivalent form |
|---|---|---|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `|=` | `x |= 3` | `x = x | 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `>>=` | `x >>= 3` | `x = x >> 3` |
| `<<=` | `x <<= 3` | `x = x << 3` |
| `:=` | `x := 3` | Assigns inside an expression |

```python
score = 10
score += 5
print(score)  # 15

score -= 3
print(score)  # 12

score *= 2
print(score)  # 24

score /= 4
print(score)  # 6.0
```

### Walrus operator `:=`

```python
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
```

Beginner-friendly alternative:

```python
count = len(numbers)

if count > 3:
    print(f"List has {count} elements")
```

Use the normal version more often at the beginner stage.

---

## 12. Ternary Expression

A ternary expression is a short form of a simple `if...else` decision.

```python
value_if_true if condition else value_if_false
```

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

Equivalent normal form:

```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

Even or odd:

```python
number = 7
result = "Even" if number % 2 == 0 else "Odd"
```

Use a ternary expression for simple choices. Use normal `if`, `elif`, and `else` when the logic becomes complex.

---

## 13. Comparison Operators

Comparison operators return `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal | `x == y` |
| `!=` | Not equal | `x != y` |
| `>` | Greater than | `x > y` |
| `<` | Less than | `x < y` |
| `>=` | Greater than or equal | `x >= y` |
| `<=` | Less than or equal | `x <= y` |

```python
x = 5
y = 3

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```

### Chained comparisons

```python
age = 25
print(18 <= age <= 60)  # True

x = 5
print(1 < x < 10)       # True
```

This is equivalent to:

```python
age >= 18 and age <= 60
```

---

## 14. Logical Operators

Logical operators combine or reverse conditions.

| Operator | Meaning | Example |
|---|---|---|
| `and` | True only when both conditions are true | `age >= 18 and has_id` |
| `or` | True when at least one condition is true | `is_member or has_coupon` |
| `not` | Reverses the Boolean result | `not is_blocked` |

```python
age = 25
has_id = True
print(age >= 18 and has_id)  # True

has_coupon = False
is_member = True
print(has_coupon or is_member)  # True

is_blocked = False
print(not is_blocked)  # True
```

### Truth table

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

| A | `not A` |
|---|---|
| True | False |
| False | True |

### Short-circuit evaluation

- With `and`, Python stops when the first condition is false.
- With `or`, Python stops when the first condition is true.

Do not use `&&`, `||`, or `!` in Python. Use `and`, `or`, and `not`.

---

## 15. Identity Operators

Identity operators check whether two variables refer to the same object.

| Operator | Meaning |
|---|---|
| `is` | True if both references point to the same object |
| `is not` | True if they point to different objects |

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # True
print(x is y)  # False
print(x == y)  # True
```

### `==` versus `is`

- `==` checks value equality.
- `is` checks object identity.

Use identity mainly for `None` checks:

```python
value = None

if value is None:
    print("No value")
```

Prefer `is None` and `is not None` instead of `== None` and `!= None`.

---

## 16. Membership Operators

Membership operators check whether a value exists in another object.

| Operator | Meaning |
|---|---|
| `in` | True if the value exists |
| `not in` | True if the value does not exist |

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("mango" not in fruits)   # True
```

```python
text = "Hello World"
print("H" in text)       # True
print("hello" in text)   # False
print("z" not in text)   # True
```

Membership checks are case-sensitive.

Practical examples:

```python
email = "bhavana@gmail.com"
print("@gmail.com" in email)

skills = ["Python", "SQL", "Excel"]
print("Python" in skills)
```

---

## 17. Bitwise Operators

Bitwise operators work on the binary representation of integers.

| Operator | Name | Meaning |
|---|---|---|
| `&` | AND | Bit is 1 when both bits are 1 |
| `|` | OR | Bit is 1 when at least one bit is 1 |
| `^` | XOR | Bit is 1 when exactly one bit is 1 |
| `~` | NOT | Inverts bits |
| `<<` | Left shift | Shifts bits left |
| `>>` | Right shift | Shifts bits right |

```python
print(6 & 3)   # 2
print(6 | 3)   # 7
print(6 ^ 3)   # 5
print(~6)      # -7
print(6 << 2)  # 24
print(6 >> 2)  # 1
```

Binary view:

```text
6 = 0110
3 = 0011
```

```text
0110
0011
----
0010 = 2
```

```text
0110
0011
----
0111 = 7
```

```text
0110
0011
----
0101 = 5
```

Rules:

```text
~x = -(x + 1)
~6 = -7
```

```text
6 << 2 = 6 * 2^2 = 24
6 >> 2 = 6 // 2^2 = 1
```

Use logical `and`, `or`, and `not` for normal conditions. Do not replace them with bitwise operators.

---

## 18. Operator Precedence

Operator precedence determines the order in which an expression is evaluated.

```python
print(100 + 5 * 3)    # 115
print((100 + 5) * 3)  # 315
```

Multiplication occurs before addition unless parentheses change the order.

### Precedence order to remember

| Priority | Operators | Meaning |
|---:|---|---|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication and division group |
| 5 | `+`, `-` | Addition and subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `|` | Bitwise OR |
| 10 | comparisons, `is`, `in` | Comparison, identity, membership |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 | `or` | Logical OR |

Operators with the same precedence are generally evaluated left to right:

```python
print(5 + 4 - 7 + 3)  # 5
```

Exponentiation is evaluated right to left:

```python
print(2 ** 3 ** 2)  # 512
```

This means:

```text
3 ** 2 = 9
2 ** 9 = 512
```

Use parentheses when an expression may be unclear.

---

# Python Collections

## 19. Python Collections Overview

| Collection | Syntax | Ordered? | Changeable? | Duplicates? | Access style |
|---|---|---|---|---|---|
| List | `[]` | Yes | Yes | Yes | Index |
| Tuple | `()` | Yes | No | Yes | Index |
| Set | `{}` | No | Items cannot be changed directly, but items can be added or removed | No | No index |
| Frozenset | `frozenset()` | No | No | No | No index |
| Dictionary | `{key: value}` | Yes | Yes | No duplicate keys | Key |

```python
fruits_list = ["apple", "banana"]
fruits_tuple = ("apple", "banana")
fruits_set = {"apple", "banana"}
fruits_frozenset = frozenset(["apple", "banana"])
student = {"name": "Bhavana", "age": 25}
```

### Simple memory rule

- Use a **list** when order matters and values may change.
- Use a **tuple** when order matters and values should remain fixed.
- Use a **set** when values must be unique.
- Use a **frozenset** when unique values must remain fixed.
- Use a **dictionary** when each value needs a key.

---

# Lists

## 20. Python Lists

A list stores multiple items in one variable.

```python
fruits = ["apple", "banana", "cherry"]
```

Lists are:

- ordered
- changeable or mutable
- able to contain duplicate values

```python
numbers = [10, 20, 30]
mixed = ["Bhavana", 25, True, 99.5]

print(len(numbers))
print(type(numbers))
```

List constructor:

```python
fruits = list(("apple", "banana", "cherry"))
```

Duplicates are allowed:

```python
fruits = ["apple", "banana", "apple"]
```

List indexes begin at `0`.

---

## 21. Access List Items

### Positive indexing

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry
```

### Negative indexing

```python
print(fruits[-1])  # cherry
print(fruits[-2])  # banana
```

### Slicing

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

print(fruits[1:4])   # ['banana', 'cherry', 'orange']
print(fruits[:3])    # ['apple', 'banana', 'cherry']
print(fruits[2:])    # ['cherry', 'orange', 'kiwi']
print(fruits[-4:-1]) # ['banana', 'cherry', 'orange']
```

The start index is included and the end index is excluded.

### Membership

```python
print("banana" in fruits)
print("mango" in fruits)
```

---

## 22. Change List Items

Lists are mutable.

### Change one item

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)
```

### Change a range

```python
fruits = ["apple", "banana", "cherry", "orange"]
fruits[1:3] = ["mango", "kiwi"]
```

### Replace one item with multiple items

```python
fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["mango", "kiwi"]
```

### Replace multiple items with one item

```python
fruits = ["apple", "banana", "cherry", "orange"]
fruits[1:3] = ["mango"]
```

### Insert without replacing

```python
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "mango")
```

Slice assignment can increase or decrease the list length.

---

## 23. Add List Items

### `append()`

Adds one item at the end.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
```

### `insert()`

Adds one item at a specified index.

```python
fruits.insert(1, "mango")
```

### `extend()`

Adds items from another iterable.

```python
fruits = ["apple", "banana"]
more_fruits = ["cherry", "orange"]
fruits.extend(more_fruits)
```

`extend()` can accept a list, tuple, set, string, or another iterable.

### `append()` versus `extend()`

```python
fruits = ["apple", "banana"]
fruits.append(["cherry", "orange"])
print(fruits)
```

Output:

```text
['apple', 'banana', ['cherry', 'orange']]
```

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "orange"])
print(fruits)
```

Output:

```text
['apple', 'banana', 'cherry', 'orange']
```

---

## 24. Remove List Items

### `remove()`

Removes the first matching value.

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
```

Only the first matching value is removed.

### `pop()`

Removes by index and returns the removed item.

```python
fruits.pop(1)
```

Without an index, the last item is removed.

```python
fruits.pop()
```

### `del`

```python
del fruits[0]  # delete one item
del fruits     # delete the variable
```

### `clear()`

```python
fruits.clear()
```

`clear()` empties the list but keeps the variable. `del fruits` removes the variable.

---

## 25. Loop Lists

### Direct loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Index loop

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

### `while` loop

```python
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
```

Use a direct loop when only the item is needed. Do not forget to update the counter in a `while` loop.

---

## 26. List Comprehension

A list comprehension creates a new list using compact syntax.

```python
new_list = [expression for item in iterable if condition]
```

### Filter items

```python
fruits = ["apple", "banana", "cherry", "kiwi"]
new_list = [fruit for fruit in fruits if "a" in fruit]
print(new_list)
```

### Copy items into a new list

```python
new_list = [fruit for fruit in fruits]
```

### Modify items

```python
upper_fruits = [fruit.upper() for fruit in fruits]
```

### Use `range()`

```python
numbers = [x for x in range(5)]
```

### Conditional expression inside a comprehension

```python
fruits = ["apple", "banana", "cherry"]
new_list = ["orange" if fruit == "banana" else fruit for fruit in fruits]
```

Use a normal loop when a comprehension becomes difficult to read.

---

## 27. Sort Lists

### Ascending sort

```python
fruits = ["orange", "mango", "kiwi", "apple"]
fruits.sort()
```

```python
numbers = [100, 50, 65, 82, 23]
numbers.sort()
```

### Descending sort

```python
numbers.sort(reverse=True)
```

### Custom sort key

```python
def close_to_50(number):
    return abs(number - 50)

numbers.sort(key=close_to_50)
```

### Case-insensitive sort

```python
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort(key=str.lower)
```

### `reverse()`

```python
fruits.reverse()
```

`reverse()` reverses the current order. It does not sort the values. `sort()` changes the original list and does not return a new sorted list.

---

## 28. Copy Lists

### Wrong for an independent copy

```python
list1 = ["apple", "banana"]
list2 = list1
list2.append("cherry")
```

Both variables refer to the same list.

### Correct methods

```python
list2 = list1.copy()
list2 = list(list1)
list2 = list1[:]
```

```python
list1 = ["apple", "banana"]
list2 = list1.copy()
list2.append("cherry")

print(list1)  # ['apple', 'banana']
print(list2)  # ['apple', 'banana', 'cherry']
```

---

## 29. Join Lists

### Using `+`

```python
list1 = ["apple", "banana"]
list2 = ["cherry", "orange"]
list3 = list1 + list2
```

### Using `append()` in a loop

```python
for item in list2:
    list1.append(item)
```

### Using `extend()`

```python
list1.extend(list2)
```

Do not use `append(list2)` when the individual elements of `list2` should be added.

---

## 30. Important List Methods

| Method | Meaning |
|---|---|
| `append()` | Adds one item to the end |
| `clear()` | Removes all items |
| `copy()` | Returns an independent shallow copy |
| `count()` | Counts occurrences of a value |
| `extend()` | Adds values from another iterable |
| `index()` | Returns the first index of a value |
| `insert()` | Adds an item at a specified index |
| `pop()` | Removes by index, or removes the last item |
| `remove()` | Removes the first matching value |
| `reverse()` | Reverses the current order |
| `sort()` | Sorts the list |

```python
numbers = [10, 20, 30, 20]

numbers.append(40)
print(numbers)
print(numbers.count(20))
print(numbers.index(30))

numbers.remove(20)
print(numbers)

numbers.reverse()
print(numbers)
```

---

# Tuples

## 31. Python Tuples

A tuple stores multiple items in one variable and uses round brackets.

```python
fruits = ("apple", "banana", "cherry")
```

Tuples are:

- ordered
- unchangeable or immutable
- able to contain duplicates

```python
numbers = (10, 20, 30)
mixed = ("Bhavana", 25, True)

print(len(numbers))
print(type(numbers))
```

Constructor:

```python
fruits = tuple(("apple", "banana", "cherry"))
```

### One-item tuple

```python
fruit = ("apple")
print(type(fruit))  # str

fruit = ("apple",)
print(type(fruit))  # tuple
```

The comma creates the one-item tuple.

---

## 32. Access Tuple Items

Tuples support positive indexes, negative indexes, slicing, and membership checks.

```python
fruits = ("apple", "banana", "cherry")

print(fruits[0])
print(fruits[1])
print(fruits[-1])
```

```python
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
print(fruits[1:4])
```

```python
print("banana" in fruits)
```

The slicing end index is excluded.

---

## 33. Update Tuples

Tuples cannot be changed directly.

```python
# Error
fruits[1] = "mango"
```

### Workaround

1. Convert the tuple to a list.
2. Modify the list.
3. Convert the list back to a tuple.

```python
fruits = ("apple", "banana", "cherry")

temp_list = list(fruits)
temp_list[1] = "mango"
fruits = tuple(temp_list)
```

### Add using list conversion

```python
temp_list = list(fruits)
temp_list.append("cherry")
fruits = tuple(temp_list)
```

### Add tuple to tuple

```python
fruits = ("apple", "banana")
new_fruit = ("cherry",)
fruits += new_fruit
```

### Remove using list conversion

```python
temp_list = list(fruits)
temp_list.remove("banana")
fruits = tuple(temp_list)
```

### Delete the entire tuple variable

```python
del fruits
```

---

## 34. Tuple Packing and Unpacking

### Packing

```python
fruits = ("apple", "banana", "cherry")
```

### Unpacking

```python
a, b, c = fruits
```

The number of variables must match the number of tuple values unless `*` is used.

### Starred unpacking

```python
fruits = ("apple", "banana", "cherry", "orange")
first, *middle, last = fruits

print(first)   # apple
print(middle)  # ['banana', 'cherry']
print(last)    # orange
```

The starred variable receives a list.

---

## 35. Loop Tuples

```python
fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)
```

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

```python
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

## 36. Join Tuples

Use `+` to join tuples.

```python
tuple1 = ("apple", "banana")
tuple2 = ("cherry", "orange")
tuple3 = tuple1 + tuple2
```

Use `*` to repeat a tuple.

```python
fruits = ("apple", "banana")
result = fruits * 2
```

Joining creates a new tuple.

---

## 37. Tuple Methods

Tuples have two main methods.

| Method | Meaning |
|---|---|
| `count()` | Counts occurrences of a value |
| `index()` | Returns the first index of a value |

```python
numbers = (10, 20, 30, 20, 40)
print(numbers.count(20))  # 2
print(numbers.index(30))  # 2
```

Tuples do not have changing methods such as `append()`, `remove()`, or `sort()`.

---

# Sets and Frozenset

## 38. Python Sets

A set stores multiple unique values.

```python
fruits = {"apple", "banana", "cherry"}
```

Sets are:

- unordered
- unindexed
- unique
- not directly item-changeable
- able to add and remove items

```python
numbers = {10, 20, 30}
mixed = {"Bhavana", 25, True}

print(len(numbers))
print(type(numbers))
```

Constructor:

```python
fruits = set(("apple", "banana", "cherry"))
```

### Duplicate removal

```python
fruits = {"apple", "banana", "apple"}
print(fruits)
```

### Empty set

```python
my_set = set()
```

`{}` creates an empty dictionary, not an empty set.

### `True`, `1`, `False`, and `0`

```python
values = {True, 1, False, 0}
print(values)
```

`True` equals `1`, and `False` equals `0`, so the set keeps only one value from each equal pair.

---

## 39. Access Set Items

Sets do not support indexing.

```python
# Error
print(fruits[0])
```

Use a loop:

```python
for fruit in fruits:
    print(fruit)
```

Use membership checks:

```python
print("banana" in fruits)
print("mango" not in fruits)
```

Set output order is not guaranteed.

---

## 40. Add Set Items

### `add()`

Adds one item.

```python
fruits = {"apple", "banana"}
fruits.add("cherry")
```

### `update()`

Adds multiple values from another iterable.

```python
fruits.update(["cherry", "orange"])
```

Sets keep only unique values.

---

## 41. Remove Set Items

### `remove()`

```python
fruits.remove("banana")
```

Raises an error if the item is missing.

### `discard()`

```python
fruits.discard("mango")
```

Does not raise an error if the item is missing.

### `pop()`

```python
removed_item = fruits.pop()
```

Removes an unpredictable item because a set has no ordered last element.

### `clear()`

```python
fruits.clear()
```

Empties the set.

### `del`

```python
del fruits
```

Deletes the variable.

---

## 42. Loop Sets

```python
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)
```

Do not depend on a fixed set order and do not try to loop by index.

---

## 43. Join Sets and Set Operations

Set operations compare groups.

| Operation | Method | Shortcut | Result |
|---|---|---|---|
| Union | `set1.union(set2)` | `set1 | set2` | All unique items |
| Update | `set1.update(set2)` | - | Adds items and changes `set1` |
| Intersection | `set1.intersection(set2)` | `set1 & set2` | Common items |
| Intersection update | `set1.intersection_update(set2)` | - | Keeps common items in `set1` |
| Difference | `set1.difference(set2)` | `set1 - set2` | Items only in `set1` |
| Difference update | `set1.difference_update(set2)` | - | Removes `set2` items from `set1` |
| Symmetric difference | `set1.symmetric_difference(set2)` | `set1 ^ set2` | Non-common items |
| Symmetric difference update | `set1.symmetric_difference_update(set2)` | - | Keeps non-common items in `set1` |

### Union

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

result = set1.union(set2)
result = set1 | set2
```

`union()` returns a new set. `update()` changes the original set.

### Intersection

```python
python_students = {"Asha", "Bhavana", "Charan"}
sql_students = {"Bhavana", "Deepak", "Charan"}

common_students = python_students.intersection(sql_students)
common_students = python_students & sql_students
```

### Difference

```python
required_skills = {"Python", "SQL", "Git", "Django"}
my_skills = {"Python", "SQL"}

missing_skills = required_skills.difference(my_skills)
missing_skills = required_skills - my_skills
```

Difference direction matters.

### Symmetric difference

```python
result = set1.symmetric_difference(set2)
result = set1 ^ set2
```

Methods ending in `_update()` modify the original set.

---

## 44. Frozenset

A frozenset is an immutable set.

It is:

- unordered
- unique
- unchangeable

```python
skills = frozenset(["Python", "SQL", "Git"])

print(skills)
print(type(skills))
```

Changing methods are unavailable:

```python
# Error
skills.add("Django")
```

Non-changing set operations are supported:

```python
a = frozenset(["Python", "SQL"])
b = frozenset(["SQL", "Git"])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
```

---

## 45. Important Set Methods

| Method | Meaning |
|---|---|
| `add()` | Adds one item |
| `clear()` | Removes all items |
| `copy()` | Returns a copy |
| `difference()` | Items in the first set but not another |
| `difference_update()` | Removes another set's items from the current set |
| `discard()` | Removes if present; no error if missing |
| `intersection()` | Returns common items |
| `intersection_update()` | Keeps common items in the current set |
| `isdisjoint()` | Checks whether sets have no common items |
| `issubset()` | Checks whether all current items exist in another set |
| `issuperset()` | Checks whether the current set contains another set |
| `pop()` | Removes an unpredictable item |
| `remove()` | Removes an item; error if missing |
| `symmetric_difference()` | Returns items that are not common |
| `symmetric_difference_update()` | Updates with non-common items |
| `union()` | Returns all unique items |
| `update()` | Adds values from another iterable |

```python
skills = {"Python", "SQL"}
required_skills = {"Python", "SQL", "Git"}

print(skills.intersection(required_skills))
print(required_skills.difference(skills))
print(skills.issubset(required_skills))
```

Understand whether a method returns a new set or changes the existing set.

---

# Dictionaries

## 46. Python Dictionaries

A dictionary stores key-value pairs.

```python
student = {
    "name": "Bhavana",
    "age": 25,
    "city": "Hyderabad"
}
```

- `"name"`, `"age"`, and `"city"` are keys.
- Their associated data are values.

Dictionaries are:

- ordered
- changeable
- unable to keep duplicate keys

```python
print(len(student))
print(type(student))
```

Constructor:

```python
student = dict(name="Bhavana", age=25, city="Hyderabad")
```

### Duplicate keys

```python
student = {
    "name": "Bhavana",
    "age": 25,
    "age": 26
}
```

The second `"age"` value overwrites the first.

---

## 47. Access Dictionary Items

### Square brackets

```python
print(student["name"])
```

Use this when the key definitely exists.

### `get()`

```python
print(student.get("city"))
```

If the key is missing, `get()` returns `None` by default instead of raising a `KeyError`.

```python
print(student.get("email"))  # None
```

### `keys()`

```python
print(student.keys())
```

### `values()`

```python
print(student.values())
```

### `items()`

```python
print(student.items())
```

Each item is a key-value tuple.

### Check whether a key exists

```python
if "age" in student:
    print("Age is available")
```

`in` checks keys by default.

To check a value:

```python
print("Bhavana" in student.values())
```

---

## 48. Change Dictionary Items

### Key assignment

```python
student["age"] = 26
```

### `update()`

```python
student.update({"city": "Bengaluru"})
```

If the assigned key does not exist, a new key-value pair is added.

---

## 49. Add Dictionary Items

### New key assignment

```python
student["city"] = "Hyderabad"
```

### `update()`

```python
student.update({"goal": "Python job preparation"})
```

String keys require quotes.

---

## 50. Remove Dictionary Items

### `pop()`

Removes a specified key.

```python
student.pop("age")
```

### `popitem()`

Removes the last inserted item.

```python
student.popitem()
```

### `del`

```python
del student["city"]  # remove one key
del student          # delete the dictionary variable
```

### `clear()`

```python
student.clear()
```

Empties the dictionary but keeps the variable.

---

## 51. Loop Dictionaries

### Loop through keys

```python
for key in student:
    print(key)
```

### Loop through values using keys

```python
for key in student:
    print(student[key])
```

### Loop through values

```python
for value in student.values():
    print(value)
```

### Loop through key-value pairs

```python
for key, value in student.items():
    print(key, ":", value)
```

A direct dictionary loop produces keys.

---

## 52. Copy Dictionaries

### Wrong for an independent copy

```python
student2 = student1
```

Both variables refer to the same dictionary.

### Correct methods

```python
student2 = student1.copy()
student2 = dict(student1)
```

```python
student1 = {"name": "Bhavana", "age": 25}
student2 = student1.copy()
student2["age"] = 26

print(student1)  # age remains 25
print(student2)  # age becomes 26
```

---

## 53. Nested Dictionaries

A nested dictionary contains dictionaries as values.

```python
students = {
    "student1": {
        "name": "Bhavana",
        "age": 25
    },
    "student2": {
        "name": "Asha",
        "age": 24
    }
}
```

Access nested values with multiple keys:

```python
print(students["student1"]["name"])
print(students["student2"]["age"])
```

Loop through nested dictionaries:

```python
for student_id, details in students.items():
    print(student_id)

    for key, value in details.items():
        print(key, ":", value)
```

---

## 54. Important Dictionary Methods

| Method | Meaning |
|---|---|
| `clear()` | Removes all items |
| `copy()` | Returns an independent shallow copy |
| `fromkeys()` | Creates a dictionary from keys and one value |
| `get()` | Returns a value safely |
| `items()` | Returns key-value pairs |
| `keys()` | Returns keys |
| `pop()` | Removes by key |
| `popitem()` | Removes the last inserted pair |
| `setdefault()` | Returns a value; inserts a default if missing |
| `update()` | Changes or adds key-value pairs |
| `values()` | Returns values |

```python
student = {
    "name": "Bhavana",
    "age": 25
}

print(student.get("name"))

student.setdefault("city", "Hyderabad")
print(student)

student.update({"age": 26})
print(student)

print(student.keys())
print(student.values())
print(student.items())
```

Use `get()` when a key may be missing. Use `setdefault()` when a missing key should also be inserted with a default value.

---

## 55. Master Revision Code

Create a file named `day2_part1_part2_revision.py`.

```python
# Day 02 Combined Revision
# Booleans, Operators, Lists, Tuples, Sets, Frozenset, and Dictionaries

# --------------------------------------------------
# 1. BOOLEANS
# --------------------------------------------------

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool("False"))
print(bool("0"))


def is_adult(age):
    return age >= 18


age = 21

if is_adult(age):
    print("Adult")
else:
    print("Minor")

x = 200
print(isinstance(x, int))

# --------------------------------------------------
# 2. OPERATORS
# --------------------------------------------------

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

score = 10
score += 5
print(score)
score -= 3
print(score)
score *= 2
print(score)
score /= 4
print(score)

num = 6
day_type = "WEEKEND!" if num > 5 else "Workday"
print(day_type)

age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(1 < x < 10)

age = 25
has_id = True
print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)

list1 = ["apple", "banana"]
list2 = ["apple", "banana"]
list3 = list1
print(list1 is list3)
print(list1 is list2)
print(list1 == list2)

value = None
print(value is None)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~6)
print(6 << 2)
print(6 >> 2)

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print((100 + 5) * 3)
print(5 + 4 - 7 + 3)
print(2 ** 3 ** 2)

# --------------------------------------------------
# 3. LISTS
# --------------------------------------------------

fruits = ["apple", "banana", "cherry", "banana"]
print("Original list:", fruits)
print("Length:", len(fruits))
print("Type:", type(fruits))
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Slice:", fruits[1:3])
print("banana" in fruits)
print("mango" not in fruits)

fruits[1] = "mango"
print("After changing index 1:", fruits)

fruits[1:3] = ["kiwi", "orange"]
print("After changing range:", fruits)

fruits.append("grapes")
fruits.insert(1, "pineapple")
fruits.extend(["watermelon", "papaya"])
print("After adding items:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

last_item = fruits.pop()
print("Popped item:", last_item)
print("After pop:", fruits)

del fruits[0]
print("After del index 0:", fruits)

for fruit in fruits:
    print("Fruit:", fruit)

for i in range(len(fruits)):
    print(i, fruits[i])

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
squares = [num ** 2 for num in numbers]
print("Even numbers:", even_numbers)
print("Squares:", squares)

marks = [80, 45, 90, 60]
marks.sort()
print("Sorted marks:", marks)
marks.sort(reverse=True)
print("Descending marks:", marks)

marks_copy = marks.copy()
marks_copy.append(100)
print("Original marks:", marks)
print("Copied marks:", marks_copy)

list_a = ["Python", "SQL"]
list_b = ["Excel", "Git"]
skills = list_a + list_b
print("Joined skills:", skills)

# --------------------------------------------------
# 4. TUPLES
# --------------------------------------------------

student_tuple = ("Bhavana", 25, "Hyderabad")
print("Tuple:", student_tuple)
print("Length:", len(student_tuple))
print("Type:", type(student_tuple))
print("Name:", student_tuple[0])
print("City:", student_tuple[-1])

single_item_tuple = ("Python",)
print(type(single_item_tuple))

name, age, city = student_tuple
print("Name:", name)
print("Age:", age)
print("City:", city)

fruits_tuple = ("apple", "banana", "cherry", "orange")
first, *middle, last = fruits_tuple
print("First:", first)
print("Middle:", middle)
print("Last:", last)

fruits_list = list(fruits_tuple)
fruits_list.append("kiwi")
fruits_tuple = tuple(fruits_list)
print("Updated tuple:", fruits_tuple)

tuple1 = ("Python", "SQL")
tuple2 = ("Git", "Django")
tuple3 = tuple1 + tuple2
print("Joined tuple:", tuple3)
print("Repeated tuple:", tuple1 * 2)

numbers_tuple = (10, 20, 30, 20, 40)
print(numbers_tuple.count(20))
print(numbers_tuple.index(30))

# --------------------------------------------------
# 5. SETS
# --------------------------------------------------

skills = {"Python", "SQL", "Python", "Git"}
print("Set:", skills)
print("Length:", len(skills))
print("Type:", type(skills))

empty_set = set()
print(type(empty_set))

print("Python" in skills)
print("Excel" not in skills)

skills.add("Django")
print("After add:", skills)

skills.update(["HTML", "CSS"])
print("After update:", skills)

skills.discard("CSS")
print("After discard:", skills)

for skill in skills:
    print("Skill:", skill)

python_students = {"Asha", "Bhavana", "Charan"}
sql_students = {"Bhavana", "Deepak", "Charan"}

all_students = python_students.union(sql_students)
common_students = python_students.intersection(sql_students)
only_python_students = python_students.difference(sql_students)
not_common_students = python_students.symmetric_difference(sql_students)

print("All students:", all_students)
print("Common students:", common_students)
print("Only Python students:", only_python_students)
print("Not common students:", not_common_students)

fixed_skills = frozenset(["Python", "SQL", "Git"])
print("Frozenset:", fixed_skills)

# --------------------------------------------------
# 6. DICTIONARIES
# --------------------------------------------------

student = {
    "name": "Bhavana",
    "age": 25,
    "city": "Hyderabad",
    "skills": ["Python", "SQL"]
}

print("Dictionary:", student)
print("Length:", len(student))
print("Type:", type(student))
print(student["name"])
print(student.get("city"))
print(student.keys())
print(student.values())
print(student.items())

if "age" in student:
    print("Age key exists")

student["age"] = 26
print("After age update:", student)

student["goal"] = "Python job preparation"
print("After adding goal:", student)

student.update({"city": "Bengaluru"})
print("After city update:", student)

student.pop("goal")
print("After pop:", student)

for key in student:
    print("Key:", key)

for value in student.values():
    print("Value:", value)

for key, value in student.items():
    print(key, ":", value)

student_copy = student.copy()
student_copy["age"] = 30
print("Original student:", student)
print("Copied student:", student_copy)

students = {
    "student1": {
        "name": "Bhavana",
        "age": 25
    },
    "student2": {
        "name": "Asha",
        "age": 24
    }
}

print(students["student1"]["name"])

for student_id, details in students.items():
    print(student_id)

    for key, value in details.items():
        print(key, ":", value)
```

Type this program, run it section by section, examine each output, and change values to test your understanding.

---

## 56. Must-Remember Points

### Booleans

- Boolean values are `True` and `False`.
- `bool()` checks truthiness and falsiness.
- Empty strings, empty collections, `0`, `None`, and `False` are falsy.
- `"False"` and `"0"` are truthy because they are non-empty strings.
- Functions can return Boolean values.
- `isinstance()` returns a Boolean result.

### Operators

- `/` returns a float.
- `//` performs floor division.
- `%` returns the remainder.
- `**` performs exponentiation.
- `+=`, `-=`, `*=`, and similar operators update variables.
- Ternary expressions are useful for simple two-way choices.
- Comparison operators return Boolean results.
- `and`, `or`, and `not` combine or reverse conditions.
- `==` checks value equality; `is` checks object identity.
- Use `is None` to check `None`.
- `in` and `not in` perform membership checks.
- Bitwise operators operate on binary values.
- Parentheses make precedence clear.

### Lists

- Lists are ordered, mutable, and allow duplicates.
- Indexing begins at `0`.
- Slicing includes the start and excludes the end.
- `append()` adds one item; `extend()` adds multiple items.
- `remove()` removes the first matching value.
- `pop()` removes by index or removes the last value.
- `clear()` empties the list; `del` can remove an item or the variable.
- List comprehensions create new lists.
- `sort()` sorts; `reverse()` reverses the current order.
- Use `copy()`, `list()`, or slicing for an independent copy.

### Tuples

- Tuples are ordered, immutable, and allow duplicates.
- A one-item tuple requires a comma.
- Tuples support indexes, slices, and membership checks.
- Convert to a list when a tuple must be modified.
- Unpacking extracts values into variables.
- Starred unpacking collects remaining values in a list.
- `+` joins tuples; `*` repeats them.
- Tuple methods are `count()` and `index()`.

### Sets and frozenset

- Sets are unordered, unindexed, and unique.
- Create an empty set with `set()`.
- `add()` adds one item; `update()` adds multiple items.
- `remove()` errors if missing; `discard()` does not.
- Set `pop()` removes an unpredictable item.
- `union()` returns all unique items.
- `intersection()` returns common items.
- `difference()` is directional.
- `symmetric_difference()` returns non-common items.
- Frozensets are immutable sets.

### Dictionaries

- Dictionaries store key-value pairs.
- Keys must be unique; later duplicate keys overwrite earlier values.
- Access values using keys.
- `get()` is safer when a key may be missing.
- `keys()`, `values()`, and `items()` inspect dictionary data.
- `in` checks keys by default.
- `update()` changes or adds pairs.
- `pop()` removes by key; `popitem()` removes the last inserted item.
- Use `copy()` or `dict()` for an independent copy.
- Nested dictionaries require multiple keys for nested access.

---

## 57. Beginner Mistakes to Avoid

### Boolean mistakes

- Writing `true`, `false`, or `none` instead of `True`, `False`, or `None`.
- Confusing `=` and `==`.
- Thinking `"False"` or `"0"` is falsy.
- Writing `if condition == True:` when `if condition:` is clearer.

### Operator mistakes

- Thinking `/` returns an integer.
- Treating `%` as percentage rather than remainder.
- Assuming `//` only removes decimals for negative numbers.
- Writing `x =+ 3` instead of `x += 3`.
- Using `&&`, `||`, or `!` instead of Python keywords.
- Using `is` for normal value comparison.
- Using `&` instead of `and` in normal conditions.
- Ignoring operator precedence.

### List mistakes

- Thinking indexing starts from `1`.
- Using an out-of-range index.
- Including the slicing end index mentally.
- Confusing `append()` and `extend()`.
- Using `=` when an independent list copy is needed.
- Thinking `sort()` creates and returns a new list.
- Thinking `reverse()` sorts values.

### Tuple mistakes

- Forgetting the comma in a one-item tuple.
- Trying to change a tuple directly.
- Using the wrong number of unpacking variables.
- Forgetting that starred unpacking returns a list.

### Set mistakes

- Assuming sets preserve a useful order.
- Accessing a set by index.
- Creating an empty set with `{}`.
- Using `remove()` when an item may be missing.
- Thinking set `pop()` removes a last item.
- Forgetting that duplicate values are removed.
- Forgetting that `True == 1` and `False == 0`.

### Dictionary mistakes

- Accessing a possibly missing key with `[]`.
- Expecting duplicate keys to be preserved.
- Thinking `in` checks values by default.
- Copying a dictionary with `=` when independence is required.
- Confusing dictionary keys with list indexes.
- Forgetting that nested dictionary access needs multiple keys.

---

## 58. Practice Problems

### A. Booleans and conditions

1. Print the result of `20 > 10`.
2. Print the result of `20 == 10`.
3. Print the result of `20 < 10`.
4. Store your age and check whether you are an adult.
5. Use `bool()` on `"Python"`, `""`, `100`, `0`, `[]`, `[1, 2]`, `"False"`, and `"0"`.
6. Create `is_even(number)` that returns `True` for even numbers.
7. Create `is_valid_email(email)` that checks whether `"@"` exists.
8. Use `isinstance()` to check whether `25` is an integer.
9. Use `isinstance()` to check whether `"25"` is a string.
10. Create a Boolean variable named `has_completed_day2`.

### B. Arithmetic and assignment operators

11. Create `x = 15` and `y = 4`, then print all arithmetic results.
12. Find the remainder of `25 / 7` using `%`.
13. Find the floor-division result of `25 // 7`.
14. Calculate `2 ** 5`.
15. Check whether `45` is even or odd using `%`.
16. Convert `135` minutes into hours and remaining minutes using `//` and `%`.
17. Start with `score = 10`, then add `5` using `+=`.
18. Start with `balance = 1000`, then subtract `250` using `-=`.
19. Start with `price = 100`, then multiply by `2` using `*=`.
20. Start with `total = 500`, then divide by `5` using `/=`.
21. Start with `number = 10`, then apply `%= 3`.
22. Start with `power = 2`, then apply `**= 4`.

### C. Ternary, comparison, and logical operators

23. Given `age = 20`, store `"Adult"` if age is at least 18, otherwise `"Minor"`.
24. Given `marks = 75`, store `"Pass"` if marks are at least 35, otherwise `"Fail"`.
25. Given `num = 10`, store `"Even"` if the number is even, otherwise `"Odd"`.
26. Compare two numbers using every comparison operator.
27. Check whether a number is between 1 and 100.
28. Check whether age is between 18 and 60.
29. Check whether a user can enter if `age >= 18` and `has_id` is true.
30. Check whether a student passed if marks are greater than 35 or grace marks are available.
31. Use `not` to reverse a Boolean value.
32. Check whether a username is not empty and password length is at least 8.

### D. Identity, membership, bitwise, and precedence

33. Create two equal lists and check them using `==`.
34. Create two equal lists and check them using `is`.
35. Assign one list to another variable and check `is`.
36. Check whether a variable is `None`.
37. Check whether `"banana"` exists in a fruits list.
38. Check whether `"Python"` exists in a sentence.
39. Check whether an email contains `"@gmail.com"`.
40. Print `6 & 3`.
41. Print `6 | 3`.
42. Print `6 ^ 3`.
43. Print `~6`.
44. Print `6 << 2`.
45. Print `6 >> 2`.
46. Predict the output of `10 + 5 * 2`.
47. Predict the output of `(10 + 5) * 2`.
48. Predict the output of `2 ** 3 ** 2`.

### E. Lists

49. Create a list of five fruits.
50. Print the first item.
51. Print the last item using negative indexing.
52. Print the list length.
53. Check whether `"apple"` exists.
54. Add `"mango"` to the end.
55. Insert `"kiwi"` at index `1`.
56. Extend the list with two more fruits.
57. Change the second item.
58. Change a range of two items.
59. Remove a fruit using `remove()`.
60. Remove the last item using `pop()`.
61. Delete the first item using `del`.
62. Empty a list using `clear()`.
63. Loop through a list using a direct `for` loop.
64. Loop through a list using indexes.
65. Create a list of numbers and print only even numbers.
66. Create a list of squares using list comprehension.
67. Sort marks in ascending order.
68. Sort marks in descending order.
69. Copy a list correctly and prove that changing the copy does not change the original.
70. Join two lists using `+`.
71. Join two lists using `extend()`.

### F. List comprehension

72. From `words = ["apple", "banana", "kiwi", "mango", "cherry"]`, create a list containing only words with `"a"`.
73. Create numbers from `0` to `10` using `range()`.
74. Create even numbers from `0` to `20`.
75. Convert `names = ["bhavana", "asha", "charan"]` to uppercase.
76. Replace `"banana"` with `"orange"` using list comprehension.

### G. Tuples

77. Create a tuple of four cities.
78. Print the first city.
79. Print the last city.
80. Print a slice of the tuple.
81. Check whether `"Hyderabad"` exists.
82. Create a one-item tuple correctly.
83. Create a one-item value without a comma and check its type.
84. Unpack a tuple into variables.
85. Use `*` while unpacking.
86. Convert a tuple to a list, change one item, and convert it back.
87. Add one item to a tuple using tuple addition.
88. Join two tuples.
89. Multiply a tuple by `3`.
90. Use `count()` on a tuple.
91. Use `index()` on a tuple.

### H. Sets

92. Create a set of skills.
93. Add one skill using `add()`.
94. Add multiple skills using `update()`.
95. Check whether `"Python"` exists.
96. Remove an item using `remove()`.
97. Remove an item using `discard()`.
98. Try removing a missing item with `remove()` and understand the error.
99. Use `pop()` and observe which item is removed.
100. Empty a set using `clear()`.
101. Create an empty set correctly.
102. Create a set with duplicate values and observe the result.
103. Create a set containing `True`, `1`, `False`, and `0`; observe the result.
104. Loop through a set.

### I. Set operations

105. Create Python-student and SQL-student sets.
106. Find all students using `union()`.
107. Find common students using `intersection()`.
108. Find students only in Python using `difference()`.
109. Find students not common to both using `symmetric_difference()`.
110. Repeat union using `|`.
111. Repeat intersection using `&`.
112. Repeat difference using `-`.
113. Repeat symmetric difference using `^`.
114. Use `intersection_update()` and observe the original set.
115. Use `difference_update()` and observe the original set.
116. Create a frozenset.
117. Try adding an item to a frozenset and understand the error.

### J. Dictionaries

118. Create a student dictionary with `name`, `age`, `city`, and `skills`.
119. Print the student's name.
120. Print the student's city using `get()`.
121. Print all keys.
122. Print all values.
123. Print all key-value pairs.
124. Check whether `"age"` exists as a key.
125. Change the age.
126. Add a new key named `"goal"`.
127. Update the city using `update()`.
128. Remove a key using `pop()`.
129. Remove the last inserted pair using `popitem()`.
130. Delete one key using `del`.
131. Empty a dictionary using `clear()`.
132. Loop through dictionary keys.
133. Loop through dictionary values.
134. Loop through dictionary key-value pairs.
135. Copy a dictionary correctly.
136. Prove that changing the copy does not change the original.
137. Create a nested dictionary for two students.
138. Access one nested value.
139. Loop through a nested dictionary.

---

## 59. Mini Projects

### Mini Project 1: Age Eligibility Checker

Concepts:

- Booleans
- comparison operators
- logical operators
- ternary expression
- f-strings

```python
name = "Bhavana"
age = 25
has_id = True

is_eligible = age >= 18 and has_id
status = "Allowed" if is_eligible else "Not allowed"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Has ID: {has_id}")
print(f"Status: {status}")
```

Do not use `&` where normal logical `and` is required.

### Mini Project 2: Even or Odd Checker

Concepts:

- modulus
- comparison
- ternary expression

```python
number = 27
result = "Even" if number % 2 == 0 else "Odd"

print(f"Number: {number}")
print(f"Result: {result}")
```

`%` returns the remainder; it is not a percentage operator.

### Mini Project 3: Time Converter

Convert total seconds into hours, minutes, and seconds.

```python
total_seconds = 3675

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Total seconds: {total_seconds}")
print(f"Time: {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
```

Expected result:

```text
Total seconds: 3675
Time: 1 hour(s), 1 minute(s), 15 second(s)
```

Use `//` for whole units and `%` for remaining units.

### Mini Project 4: To-Do List Manager

Concepts:

- list
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `len()`
- `for` loop
- membership checking

```python
tasks = ["Practice Python", "Read W3Schools", "Write notes"]

tasks.append("Solve exercises")
tasks.insert(1, "Revise Day 1")

if "Read W3Schools" in tasks:
    print("Study task is available")

tasks.remove("Write notes")
completed_task = tasks.pop(0)

print(f"Completed task: {completed_task}")
print(f"Remaining tasks: {len(tasks)}")

for task in tasks:
    print("-", task)
```

`pop(0)` removes the first item.

### Mini Project 5: Marks Analyzer

Concepts:

- list
- `sort()`
- `sum()`
- `len()`
- `max()`
- `min()`
- f-strings

```python
marks = [80, 95, 67, 45, 88]

total = sum(marks)
average = total / len(marks)
marks.sort(reverse=True)

print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")
```

Remember that `sort()` changes the original list.

### Mini Project 6: Unique Skills Tracker

Concepts:

- set
- `add()`
- `update()`
- membership
- `union()`
- `difference()`
- `intersection()`

```python
my_skills = {"Python", "SQL", "Excel"}
required_skills = {"Python", "SQL", "Git", "Django"}

my_skills.add("HTML")
my_skills.update(["CSS", "Git"])

matched_skills = my_skills.intersection(required_skills)
missing_skills = required_skills.difference(my_skills)
all_skills = my_skills.union(required_skills)

print("My skills:", my_skills)
print("Required skills:", required_skills)
print("Matched skills:", matched_skills)
print("Missing skills:", missing_skills)
print("All skills:", all_skills)
```

Set output order is not guaranteed.

### Mini Project 7: Student Profile Dictionary

Concepts:

- dictionary
- `keys()`
- `values()`
- `items()`
- `get()`
- `update()`
- loop

```python
student = {
    "name": "Bhavana",
    "age": 25,
    "city": "Hyderabad",
    "course": "Python"
}

student.update({"goal": "Job preparation"})
student["age"] = 26

print("Student Profile")

for key, value in student.items():
    print(f"{key}: {value}")

print("City:", student.get("city"))
```

### Mini Project 8: Contact Book

Concepts:

- dictionary
- nested dictionary
- add item
- access nested item
- nested loop

```python
contacts = {
    "bhavana": {
        "phone": "9999999999",
        "email": "bhavana@gmail.com"
    },
    "asha": {
        "phone": "8888888888",
        "email": "asha@gmail.com"
    }
}

contacts["charan"] = {
    "phone": "7777777777",
    "email": "charan@gmail.com"
}

print("Bhavana email:", contacts["bhavana"]["email"])

for name, details in contacts.items():
    print("Name:", name)

    for key, value in details.items():
        print(key, ":", value)
```

Nested values require multiple keys.

### Mini Project 9: Simple Shopping Cart

Concepts:

- list
- dictionary
- loop
- arithmetic
- f-strings

```python
cart = [
    {
        "product": "Notebook",
        "price": 50,
        "quantity": 2
    },
    {
        "product": "Pen",
        "price": 10,
        "quantity": 5
    },
    {
        "product": "Bag",
        "price": 800,
        "quantity": 1
    }
]

total = 0

for item in cart:
    item_total = item["price"] * item["quantity"]
    total += item_total
    print(f"{item['product']}: {item['quantity']} x {item['price']} = {item_total}")

print(f"Cart total: {total}")
```

Expected output:

```text
Notebook: 2 x 50 = 100
Pen: 5 x 10 = 50
Bag: 1 x 800 = 800
Cart total: 950
```

The running `total` must be updated inside the loop.

---

## 60. Interview Questions

### Booleans

1. What is a Boolean in Python?
2. What are the two Boolean values?
3. What is the difference between `True` and `"True"`?
4. What does `bool()` do?
5. What is the output of `bool("")`?
6. What is the output of `bool("False")`?
7. What is the output of `bool(0)`?
8. What is the output of `bool([])`?
9. What are truthy and falsy values?
10. Can a function return a Boolean?
11. What does `isinstance()` return?

### Operators

12. What is an operator?
13. What is an operand?
14. What are arithmetic operators?
15. What are assignment operators?
16. What are comparison operators?
17. What are logical operators?
18. What are identity operators?
19. What are membership operators?
20. What are bitwise operators?
21. What is the difference between `/` and `//`?
22. What does `%` do?
23. How do you check whether a number is even?
24. What does `**` do?
25. What does `x += 3` mean?
26. What is the walrus operator?
27. What is a ternary expression?
28. What is the syntax of a ternary expression?
29. What is the difference between `=` and `==`?
30. What is comparison chaining?
31. What does `and` do?
32. What does `or` do?
33. What does `not` do?
34. What is short-circuit evaluation?
35. What is the difference between `is` and `==`?
36. How should you check whether a value is `None`?
37. What does `in` do?
38. Is membership checking case-sensitive?
39. What do bitwise operators work on?
40. What is operator precedence?

### Lists

41. What is a list?
42. How do you create a list?
43. Are lists ordered?
44. Are lists changeable?
45. Do lists allow duplicates?
46. How do you access the first item of a list?
47. What is negative indexing?
48. What does `list[-1]` return?
49. What is slicing?
50. Is the end index included in list slicing?
51. How do you check whether an item exists in a list?
52. What does `append()` do?
53. What does `insert()` do?
54. What does `extend()` do?
55. What is the difference between `append()` and `extend()`?
56. What does `remove()` do?
57. What happens when `remove()` finds duplicate values?
58. What does `pop()` do?
59. What does `pop()` do if no index is supplied?
60. What does `del` do?
61. What does `clear()` do?
62. What is the difference between `clear()` and `del`?
63. How do you loop through a list?
64. What is list comprehension?
65. What is the syntax of list comprehension?
66. What does `sort()` do?
67. What does `sort(reverse=True)` do?
68. What does `reverse()` do?
69. What is the difference between `sort()` and `reverse()`?
70. How do you copy a list correctly?
71. Why is `list2 = list1` not an independent copy?
72. How do you join two lists?

### Tuples

73. What is a tuple?
74. How do you create a tuple?
75. Are tuples ordered?
76. Are tuples changeable?
77. Do tuples allow duplicates?
78. How do you create a one-item tuple?
79. Why is the comma important in a one-item tuple?
80. How do you access tuple items?
81. Can you change a tuple directly?
82. How can you update a tuple using a workaround?
83. How do you add an item to a tuple?
84. How do you remove an item from a tuple?
85. What is tuple packing?
86. What is tuple unpacking?
87. What happens if the number of variables does not match the number of tuple values?
88. What does `*` do in tuple unpacking?
89. How do you loop through a tuple?
90. How do you join two tuples?
91. What does multiplying a tuple do?
92. What are the two tuple methods?

### Sets and frozenset

93. What is a set?
94. How do you create a set?
95. Are sets ordered?
96. Are sets indexed?
97. Do sets allow duplicates?
98. Can set items be changed?
99. Can you add and remove set items?
100. How do you create an empty set?
101. Why does `{}` not create an empty set?
102. How do you check whether an item exists in a set?
103. What does `add()` do?
104. What does `update()` do?
105. What is the difference between `add()` and `update()`?
106. What does `remove()` do?
107. What happens when `remove()` is used on a missing item?
108. What does `discard()` do?
109. What is the difference between `remove()` and `discard()`?
110. What does `pop()` do in a set?
111. Why is set `pop()` unpredictable?
112. What does `union()` do?
113. What does `intersection()` do?
114. What does `difference()` do?
115. What does `symmetric_difference()` do?
116. What is the difference between `union()` and `update()`?
117. Why are `True` and `1` considered duplicates in a set?
118. What is a frozenset?
119. Can you add items to a frozenset?

### Dictionaries

120. What is a dictionary?
121. How do you create a dictionary?
122. What is a key-value pair?
123. Are dictionaries ordered?
124. Are dictionaries changeable?
125. Do dictionaries allow duplicate keys?
126. What happens if duplicate keys are used?
127. How do you access a dictionary value?
128. What is the difference between `dictionary["key"]` and `dictionary.get("key")`?
129. What does `keys()` return?
130. What does `values()` return?
131. What does `items()` return?
132. How do you check whether a key exists?
133. Does `in` check keys or values by default?
134. How do you change a dictionary value?
135. How do you add a new dictionary item?
136. What does `update()` do?
137. What does `pop()` do?
138. What does `popitem()` do?
139. What does `del` do in dictionaries?
140. What does `clear()` do?
141. How do you loop through dictionary keys?
142. How do you loop through dictionary values?
143. How do you loop through key-value pairs?
144. How do you copy a dictionary correctly?
145. Why is `dict2 = dict1` not an independent copy?
146. What is a nested dictionary?
147. How do you access values inside a nested dictionary?
148. How do you loop through a nested dictionary?

---

## 61. Final Day 2 Checklist

### Booleans

- [ ] I understand `True` and `False`.
- [ ] I can use `bool()`.
- [ ] I can identify truthy and falsy values.
- [ ] I can use comparison expressions.
- [ ] I can use Boolean results in conditions.
- [ ] I can write functions that return Booleans.
- [ ] I can use `isinstance()`.

### Operators

- [ ] I can use arithmetic operators.
- [ ] I can explain `/` versus `//`.
- [ ] I can use `%` for remainders and even/odd checks.
- [ ] I can use `**` for powers.
- [ ] I can use assignment operators such as `+=` and `-=`.
- [ ] I understand the walrus operator at a basic level.
- [ ] I can write simple ternary expressions.
- [ ] I can use comparison operators correctly.
- [ ] I can use chained comparisons.
- [ ] I can use `and`, `or`, and `not`.
- [ ] I understand short-circuiting at a basic level.
- [ ] I can explain `is` versus `==`.
- [ ] I can use `is None` correctly.
- [ ] I can use `in` and `not in`.
- [ ] I understand bitwise operators at a beginner level.
- [ ] I understand operator precedence.
- [ ] I can use parentheses to make expressions clear.

### Lists

- [ ] I can create a list.
- [ ] I can use positive and negative indexes.
- [ ] I can slice a list.
- [ ] I can change list items and ranges.
- [ ] I can add values with `append()`, `insert()`, and `extend()`.
- [ ] I can remove values with `remove()`, `pop()`, `del`, and `clear()`.
- [ ] I can loop through a list.
- [ ] I can use list comprehension.
- [ ] I can sort and reverse a list.
- [ ] I can copy a list correctly.
- [ ] I can join lists.

### Tuples

- [ ] I can create a tuple.
- [ ] I can create a one-item tuple correctly.
- [ ] I can access and slice tuple items.
- [ ] I understand tuple immutability.
- [ ] I can update a tuple using list conversion.
- [ ] I can add tuple to tuple.
- [ ] I can unpack a tuple.
- [ ] I can use starred unpacking.
- [ ] I can loop through a tuple.
- [ ] I can join and multiply tuples.
- [ ] I can use `count()` and `index()`.

### Sets and frozenset

- [ ] I can create a set and an empty set.
- [ ] I understand that sets are unordered and unindexed.
- [ ] I understand that sets remove duplicates.
- [ ] I can use `add()` and `update()`.
- [ ] I can use `remove()`, `discard()`, `pop()`, `clear()`, and `del`.
- [ ] I can loop through a set.
- [ ] I can use union, intersection, difference, and symmetric difference.
- [ ] I understand frozenset.

### Dictionaries

- [ ] I can create a dictionary.
- [ ] I understand key-value pairs.
- [ ] I can access values using keys and `get()`.
- [ ] I can use `keys()`, `values()`, and `items()`.
- [ ] I can check whether a key exists.
- [ ] I can change and add dictionary items.
- [ ] I can remove items using `pop()`, `popitem()`, `del`, and `clear()`.
- [ ] I can loop through keys, values, and pairs.
- [ ] I can copy dictionaries correctly.
- [ ] I can create, access, and loop through nested dictionaries.

---

## Final Practice Task

Create a file named:

```text
day2_part1_part2_full_revision_practice.py
```

Solve at least 60 problems from the Day 2 practice list, run the file, check every output, and modify values to test your understanding.
