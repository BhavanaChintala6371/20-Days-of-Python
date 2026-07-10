# Day 01 Python Revision Notes

A complete, structured revision guide covering the Day 1 Python foundation from the **1-Week Python Plan**.

## Topics Covered

1. Python Introduction
2. Python Getting Started
3. Python Syntax, Statements, and Output
4. Python Comments
5. Python Variables
6. Variable Names
7. Multiple Variable Assignment
8. Output Variables
9. Global Variables
10. Python Data Types
11. Python Numbers
12. Python Casting
13. Python Strings
14. String Indexing
15. String Length
16. Checking Strings with `in` and `not in`
17. String Slicing
18. Modifying Strings
19. String Concatenation
20. String Formatting
21. Escape Characters
22. Important String Methods to Learn First
23. One Master Revision Code Snippet
24. Must-Know Interview Questions from Day 1
25. Practice Problems and Use Cases
26. Mini Projects for Full Understanding
27. Final Day 1 Checklist

---

## 1. Python Introduction

### What Python Means

Python is a popular programming language used for:

- Web development
- Software development
- Automation
- Data handling
- Mathematics
- Scripting
- Rapid prototyping

For this learning plan, Python is mainly important for:

- Logic building
- Problem solving
- Automation
- Job preparation

A **programming language** is a way to give instructions to a computer.

**Python 3** is the current major version used for modern Python learning and development.

Python is an **interpreted language**. This means:

- Python code can run line by line.
- The Python interpreter reads and executes the code.

### Syntax

The most basic Python program is:

```python
print("Hello, World!")
```

### Example

```python
print("Hello Python!")
print("I am learning Python for job preparation")
```

### Key Points

- Python is beginner-friendly because its syntax is close to English.
- Python uses indentation instead of curly braces `{}`.
- Python usually uses new lines to separate statements.
- Python files use the `.py` extension.
- Write and run code yourself instead of only reading notes.

### Common Mistakes

#### Mistake 1: Thinking reading is enough

Reading learning material is useful, but you must also type and run the code.

#### Mistake 2: Not understanding why Python is useful

Python is not only for printing text. It is used for real applications, data, automation, backend development, AI, and problem solving.

### Practice

Write and run your first Python file using `print()`.

---

## 2. Python Getting Started

### What It Means

A **`.py` file** is a Python file.

Examples:

- `hello.py`
- `day1_basics.py`
- `practice.py`

A **text editor or IDE** is where you write code.

Examples:

- VS Code
- PyCharm
- Thonny

A **command line or terminal** is where you can run Python commands and Python files.

### Syntax

Check the installed Python version:

```bash
python --version
```

On some systems:

```bash
py --version
```

Run a Python file:

```bash
python hello.py
```

Exit the interactive Python command line:

```python
exit()
```

### Example

Create a file named `hello.py`:

```python
# hello.py
print("Hello, World!")
```

Run it from the terminal:

```bash
python hello.py
```

### Key Points

- Use the `.py` extension for Python files.
- Write code in VS Code and run it.
- The output appears in the terminal.
- `[Done] exited with code=0` means the code ran successfully.
- Python can also run short commands in the interactive Python command line.
- For learning, use `.py` files.

### Common Mistakes

#### Mistake 1: Saving the file as `.txt`

Wrong:

```text
hello.txt
```

Correct:

```text
hello.py
```

#### Mistake 2: Running the wrong file

Always check that you are running the correct file.

#### Mistake 3: Not checking the output

After running code, verify that the output matches what you expected.

### Practice

Create a `.py` file and run it from VS Code or the terminal.

---

## 3. Python Syntax, Statements, and Output

### What It Means

#### Syntax

**Syntax** means the rules for writing valid code.

Correct Python syntax:

```python
print("Hello")
```

#### Statement

A **statement** is one complete instruction.

```python
print("I am learning Python")
```

The line above is one statement.

#### Output

**Output** means what your program shows on the screen.

`print()` is used to display output.

### Syntax

```python
print("Hello")
print("Python is easy")
print(10 + 20)
```

### Example

```python
print("Hello Python!")
print("My name is Bhavana Chintala")
print("I am learning Python")

print(10 + 20)
print(50 - 40)
print(20 * 10)
print(40 / 20)

print("10 + 20")
print(10 + 20)
```

Expected output:

```text
Hello Python!
My name is Bhavana Chintala
I am learning Python
30
10
200
2.0
10 + 20
30
```

### Key Points

#### Python Uses New Lines

Good:

```python
print("Hello")
print("World")
```

Avoid writing both statements on one line:

```python
print("Hello"); print("World")
```

It may work, but it is not clean Python style.

#### Text Must Be Inside Quotes

Correct:

```python
print("Bhavana")
```

Wrong:

```python
print(Bhavana)
```

Without quotes, Python treats `Bhavana` as a variable name.

#### Text and Calculations Are Different

```python
print("10 + 20")
```

Output:

```text
10 + 20
```

Because it is inside quotes, Python treats it as text.

```python
print(10 + 20)
```

Output:

```text
30
```

Because it is not inside quotes, Python calculates it.

### Common Mistakes

#### Mistake 1: Forgetting Quotes Around Text

Wrong:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

#### Mistake 2: Confusing Text and Numbers

```python
print("50 + 10")  # Prints text
print(50 + 10)    # Prints 60
```

#### Mistake 3: Extra Unnecessary Spaces

This works:

```python
print( 20 * 10)
```

Cleaner code:

```python
print(20 * 10)
```

### Practice

Print text, numbers, and calculations.

---

## 4. Python Comments

### What It Means

A **comment** is a note inside the code. Python ignores comments while running the program.

### Syntax

A single-line comment starts with `#`:

```python
# This is a comment
print("Hello")
```

### Example

```python
# Day 01 Part 01: Python syntax, output, and comments
print("Hello Python!")

# This line prints a simple completion message
print("Day 01 Part 01 completed successfully")
```

### Key Points

- Comments help explain your code.
- Comments do not run.
- Use comments to explain why or what your code is doing.
- Keep one space after `#`.

Useful comment:

```python
# Calculate reply rate
reply_rate = 12 / 100 * 100
```

Less useful comment:

```python
# Print hello
print("Hello")
```

The second comment is too obvious.

### Common Mistakes

#### Mistake 1: Writing Comments Without `#`

Wrong:

```python
This prints my name
print("Bhavana")
```

Correct:

```python
# This prints my name
print("Bhavana")
```

#### Mistake 2: Writing Too Many Unnecessary Comments

Do not comment every simple line. Comment important logic.

### Practice

Write a program containing three useful comments.

---

## 5. Python Variables

### What It Means

A **variable** is a name used to store a value.

```python
name = "Bhavana"
age = 25
```

Here:

- `name` stores `"Bhavana"`.
- `age` stores `25`.

**Assignment** means storing a value inside a variable using `=`.

```python
city = "Hyderabad"
```

Python is **dynamically typed**, so it automatically understands the data type.

You do not need to write:

```text
int age = 25
```

In Python, write:

```python
age = 25
```

### Syntax

```python
variable_name = value
```

Examples:

```python
name = "Bhavana"
age = 25
city = "Hyderabad"
goal = "Learn Python"
```

### Example

```python
name = "Bhavana Chintala"
city = "Hyderabad"
goal = "Python job preparation"

print(name)
print(city)
print(goal)
```

### Key Points

- Variables are created when you assign a value.
- You do not need to declare the type.
- Python variables can change value.
- Python variables can also change type, but avoid doing that unnecessarily.
- Use meaningful variable names.

Good variable names:

```python
lead_count = 100
reply_count = 12
meeting_count = 3
```

Less clear names:

```python
x = 100
y = 12
z = 3
```

`x`, `y`, and `z` are acceptable for small examples, but not for clear practice code.

### Common Mistakes

#### Mistake 1: Forgetting Quotes for String Values

Wrong:

```python
name = Bhavana
```

Correct:

```python
name = "Bhavana"
```

#### Mistake 2: Using One Variable for Different Meanings

Avoid:

```python
x = 100
x = "Bhavana"
x = 12.5
```

Better:

```python
lead_count = 100
name = "Bhavana"
reply_rate = 12.5
```

### Practice

Create variables for your name, city, age, and goal.

---

## 6. Variable Names

### What It Means

A **variable name** is the name you give to a stored value.

```python
company_name = "Sharp India"
```

Here, `company_name` is the variable name.

### Recommended Style

Use **snake case** for Python variable names:

```python
company_name = "Sharp India"
lead_count = 100
```

### Example

```python
first_name = "Bhavana"
last_name = "Chintala"
city_name = "Hyderabad"

print(first_name)
print(last_name)
print(city_name)
```

### Rules for Variable Names

A variable name:

1. Must start with a letter or underscore.
2. Cannot start with a number.
3. Can contain letters, numbers, and underscores.
4. Cannot contain spaces.
5. Cannot contain hyphens.
6. Is case-sensitive.
7. Should not be a Python keyword.

### Valid Variable Names

```python
name = "Bhavana"
my_name = "Bhavana"
_name = "Bhavana"
name1 = "Bhavana"
company_name = "Sharp India"
lead_count = 100
```

### Invalid Variable Names

```text
1name = "Bhavana"
my-name = "Bhavana"
my name = "Bhavana"
```

Why they are wrong:

- `1name` starts with a number.
- `my-name` contains a hyphen.
- `my name` contains a space.

### Naming Styles

#### Snake Case

Recommended in Python:

```python
my_variable_name = "Hello"
```

#### Camel Case

Common in some other languages:

```python
myVariableName = "Hello"
```

#### Pascal Case

Usually used for class names later:

```python
MyVariableName = "Hello"
```

For Python variables, use `snake_case`.

### Case Sensitivity

These are three different variables:

```python
age = 25
Age = 30
AGE = 35

print(age)
print(Age)
print(AGE)
```

### Common Mistakes

#### Mistake 1: Using Spaces

Wrong:

```text
company name = "Sharp India"
```

Correct:

```python
company_name = "Sharp India"
```

#### Mistake 2: Starting with a Number

Wrong:

```text
1lead = 100
```

Correct:

```python
lead1 = 100
```

#### Mistake 3: Confusing Uppercase and Lowercase

```python
name = "Bhavana"
print(Name)
```

This gives an error because `name` and `Name` are different.

### Practice

Write valid and invalid variable names and explain why each one is valid or invalid.

---

## 7. Multiple Variable Assignment

### What It Means

**Multiple assignment** means assigning values to multiple variables in one line.

### Syntax

#### Many Values to Many Variables

```python
x, y, z = "Orange", "Banana", "Cherry"
```

#### One Value to Multiple Variables

```python
x = y = z = "Pending"
```

#### Unpacking

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

Unpacking becomes easier to understand after learning lists.

### Example

Many values to many variables:

```python
company_name, industry, city = "Sharp India", "Technology", "Bengaluru"

print(company_name)
print(industry)
print(city)
```

One value to multiple variables:

```python
status1 = status2 = status3 = "Pending"

print(status1)
print(status2)
print(status3)
```

Full example:

```python
name, city, goal = "Bhavana", "Hyderabad", "Learn Python"

print(name)
print(city)
print(goal)

status1 = status2 = status3 = "Pending"

print(status1)
print(status2)
print(status3)
```

### Key Points

- In many-values-to-many-variables assignment, the number of variables and values must match.
- If you have three variables, you need three values.
- One value can be assigned to many variables.
- Unpacking is useful when taking values from a collection.

### Common Mistakes

#### Mistake 1: Mismatched Count

Wrong:

```python
x, y, z = "Apple", "Banana"
```

There are three variables but only two values.

Correct:

```python
x, y, z = "Apple", "Banana", "Cherry"
```

### Practice

Assign multiple values in one line and print each variable.

---

## 8. Output Variables

### What It Means

**Outputting a variable** means printing the value stored inside it.

### Syntax

```python
name = "Bhavana"
print(name)
```

### Printing Multiple Variables with Commas

```python
x = "Python"
y = "is"
z = "awesome"

print(x, y, z)
```

Output:

```text
Python is awesome
```

### Joining Strings with `+`

```python
x = "Python "
y = "is "
z = "awesome"

print(x + y + z)
```

Output:

```text
Python is awesome
```

When using `+`, you must handle spaces manually.

### Example

```python
name = "Bhavana"
age = 25
city = "Hyderabad"

print("Name:", name)
print("Age:", age)
print("City:", city)
```

### Important Difference: `+` with Numbers and Strings

Numbers are added:

```python
x = 10
y = 20
print(x + y)
```

Output:

```text
30
```

Strings are joined:

```python
x = "10"
y = "20"
print(x + y)
```

Output:

```text
1020
```

### Key Points

- Use commas in `print()` when mixing text and numbers.
- Use `+` only when joining strings or adding numbers.
- Do not mix a string and a number with `+` unless you convert the number to a string.

### Common Mistakes

#### Mistake 1: Combining a String and Number with `+`

Wrong:

```python
age = 25
print("My age is " + age)
```

Correct with a comma:

```python
age = 25
print("My age is", age)
```

Correct with conversion:

```python
age = 25
print("My age is " + str(age))
```

Better with an f-string:

```python
age = 25
print(f"My age is {age}")
```

### Practice

Print variables using commas, `+`, and f-strings.

---

## 9. Global Variables

### What It Means

A **global variable** is created outside a function. It can be used inside and outside a function.

A **local variable** is created inside a function. It is mainly used inside that function.

The `global` keyword allows a function to create or modify a global variable.

### Syntax

A global variable used inside a function:

```python
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
```

Using `global`:

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```

### Example: Local vs Global

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)
```

Output:

```text
Python is fantastic
Python is awesome
```

Inside the function, the local `x` is used. Outside the function, the global `x` is used.

### Key Points

- A variable outside a function is global.
- A variable inside a function is local.
- `global` lets you modify a global variable inside a function.
- Do not worry too much about this topic until functions are studied properly.
- Avoid using `global` too much in real code.

### Common Mistakes

#### Mistake 1: Thinking Local and Global Variables Are Always the Same

```python
x = "global"

def test():
    x = "local"
    print(x)

test()
print(x)
```

Output:

```text
local
global
```

#### Mistake 2: Overusing `global`

For beginner-level clean code, avoid unnecessary global variables.

### Practice

Practice this topic lightly now. It will become clearer after learning functions.

---

## 10. Python Data Types

### What It Means

A **data type** tells what kind of value is stored in a variable.

### Syntax

```python
name = "Bhavana"       # str
age = 25               # int
height = 5.4           # float
is_learning = True     # bool
result = None          # NoneType
```

Check a data type using `type()`:

```python
name = "Bhavana"
age = 25
reply_rate = 12.5

print(type(name))
print(type(age))
print(type(reply_rate))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
```

### Example

```python
name = "Bhavana"
age = 25
reply_rate = 12.5
is_learning = True
future_job = None

print(type(name))
print(type(age))
print(type(reply_rate))
print(type(is_learning))
print(type(future_job))
```

### Main Data Types

| Data type | Meaning |
|---|---|
| `str` | Text |
| `int` | Whole number |
| `float` | Decimal number |
| `bool` | `True` or `False` |
| `list` | Collection of values |
| `tuple` | Ordered collection, usually fixed |
| `set` | Unique values |
| `dict` | Key-value pairs |
| `NoneType` | No value |
| `complex` | Complex number |

For Day 1, focus strongly on:

- `str`
- `int`
- `float`
- `bool`
- `NoneType`

Lists, tuples, sets, and dictionaries become more important from Day 3 onward.

### Key Points

- Python automatically identifies data types.
- Text is `str`.
- Whole numbers are `int`.
- Decimal numbers are `float`.
- `True` and `False` are Boolean values.
- `None` means no value.
- Use `type()` when you are unsure about a variable's type.

### Common Mistakes

#### Mistake 1: Thinking `"100"` and `100` Are the Same

```python
x = "100"  # string
y = 100    # integer

print(type(x))
print(type(y))
```

They are not the same.

#### Mistake 2: Forgetting Capital Letters in Boolean Values

Wrong:

```python
is_learning = true
```

Correct:

```python
is_learning = True
```

Python uses:

```python
True
False
None
```

Not:

```text
true
false
none
```

### Practice

Create variables of different types and check each one using `type()`.

---

## 11. Python Numbers

### What It Means

#### `int`

An integer is a whole number.

```python
age = 25
lead_count = 100
temperature = -5
```

#### `float`

A float is a decimal number.

```python
price = 99.99
reply_rate = 12.5
```

#### `complex`

A complex number has a real and imaginary part.

```python
x = 3 + 5j
```

Only basic awareness of `complex` is needed now.

### Syntax

```python
x = 10       # int
y = 10.5     # float
z = 3 + 5j   # complex

print(type(x))
print(type(y))
print(type(z))
```

### Arithmetic Examples

```python
print(10 + 5)  # Addition
print(10 - 5)  # Subtraction
print(10 * 5)  # Multiplication
print(10 / 5)  # Division
```

Output:

```text
15
5
50
2.0
```

Notice:

```python
print(10 / 5)
```

Output:

```text
2.0
```

It is not `2`, because `/` gives a float result.

### Scientific Notation

```python
x = 35e3
print(x)
```

Output:

```text
35000.0
```

### Random Number Basics

Import the `random` module:

```python
import random

print(random.randrange(1, 10))
```

This gives a random number from `1` up to `9`.

### Key Points

- `int` has no decimal point.
- `float` has a decimal point.
- Division using `/` gives a float result.
- `complex` uses `j`.
- Scientific notation is possible.

### Common Mistakes

#### Mistake 1: Thinking Division Always Gives an Integer

```python
print(20 / 10)
```

Output:

```text
2.0
```

#### Mistake 2: Thinking `5.0` Is an Integer

```python
x = 5.0
print(type(x))
```

Output:

```text
<class 'float'>
```

### Practice

Perform arithmetic operations and check the type of each result.

---

## 12. Python Casting

### What It Means

**Casting** means converting one data type into another.

### Syntax

```python
int()
float()
str()
```

### `int()`

Converts a value into an integer.

```python
x = int(1)
y = int(2.8)
z = int("3")

print(x)
print(y)
print(z)
```

Output:

```text
1
2
3
```

Important:

```python
print(int(2.8))
```

Output:

```text
2
```

`int()` does not round the number. It removes the decimal part.

### `float()`

Converts a value into a float.

```python
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x)
print(y)
print(z)
print(w)
```

Output:

```text
1.0
2.8
3.0
4.2
```

### `str()`

Converts a value into a string.

```python
x = str(25)
y = str(3.5)

print(x)
print(y)
print(type(x))
print(type(y))
```

Output:

```text
25
3.5
<class 'str'>
<class 'str'>
```

### Full Example

```python
x = "100"
y = 50
print(int(x) + y)

a = int(2.8)
b = float(3)
c = str(25)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
```

### Key Points

- Use `int()` when you need a whole number.
- Use `float()` when you need a decimal number.
- Use `str()` when you need text.
- `int(2.9)` gives `2`, not `3`.
- `int("3")` works.
- `int("3.5")` gives an error.
- `float("3.5")` works.
- Casting is very important when taking user input later.

### Common Mistakes

#### Mistake 1: Thinking Casting Rounds Numbers

```python
print(int(4.9))
```

Output:

```text
4
```

Not `5`.

#### Mistake 2: Adding a String Number and an Integer

Wrong:

```python
x = "100"
y = 50
print(x + y)
```

Correct:

```python
x = "100"
y = 50
print(int(x) + y)
```

#### Mistake 3: Using `int()` on a Decimal String

Wrong:

```python
x = int("3.5")
```

Correct:

```python
x = float("3.5")
```

### Practice

Convert values using `int()`, `float()`, and `str()`.

---

## 13. Python Strings

### What It Means

A **string** is text data. Strings are written inside quotes.

### Syntax

```python
name = "Bhavana"
city = 'Hyderabad'
```

Both single quotes and double quotes are valid.

For consistent practice, use double quotes:

```python
name = "Bhavana"
```

### Example

```python
name = "Bhavana"
city = "Hyderabad"

print(name)
print(city)
```

### Multiline Strings

Triple quotes are used for multiline strings:

```python
message = """I am learning Python.
This is Day 1.
Today I am studying strings."""

print(message)
```

Another example:

```python
message = """Hello Bhavana,
Welcome to Python.
Today you are learning strings."""

print(message)
```

### Quotes Inside Strings

This works because the outer quotes are double quotes and the apostrophe is inside:

```python
text = "It's a good day"
print(text)
```

This also works because the outer quotes are single quotes:

```python
text = 'She said "Hello"'
print(text)
```

### Key Points

- Strings are text.
- Text must be inside quotes.
- Single quotes and double quotes both work.
- Triple quotes are used for multiline strings.
- Strings are sequences of characters.
- Python strings are immutable, which means the original string is not changed directly.

### Common Mistakes

#### Mistake 1: Forgetting Quotes

Wrong:

```python
name = Bhavana
```

Correct:

```python
name = "Bhavana"
```

#### Mistake 2: Mixing Quotes Incorrectly

Wrong:

```text
print("She said "Hello"")
```

Correct:

```python
print('She said "Hello"')
```

Or escape the inner double quotes:

```python
print("She said \"Hello\"")
```

### Practice

Create strings using single quotes, double quotes, and triple quotes.

---

## 14. String Indexing

### What It Means

**Indexing** means accessing a character using its position.

Python indexing starts from `0`.

### Syntax

```python
text[index]
```

### Example

```python
word = "Python"

print(word[0])
print(word[1])
print(word[2])
```

Output:

```text
P
y
t
```

### Positive Index Positions

| Character | P | y | t | h | o | n |
|---|---:|---:|---:|---:|---:|---:|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |

### Negative Indexing

Negative indexing starts from the end.

```python
word = "Python"

print(word[-1])
print(word[-2])
```

Output:

```text
n
o
```

### Negative Index Positions

| Character | P | y | t | h | o | n |
|---|---:|---:|---:|---:|---:|---:|
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

### Code Snippet

```python
name = "Bhavana"

print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
```

### Key Points

- The first character is at index `0`.
- The last character is at index `-1`.
- Indexing gives one character.
- Spaces also have index positions.
- Using an index beyond the string length gives an error.

### Common Mistakes

#### Mistake 1: Thinking the Index Starts from `1`

```python
word = "Python"
print(word[1])
```

Output:

```text
y
```

It does not print `P`.

Correct first character:

```python
print(word[0])
```

#### Mistake 2: Using an Index That Does Not Exist

```python
word = "Python"
print(word[10])
```

This gives an error.

### Practice

Print the first, second, last, and second-last characters of your name.

---

## 15. String Length

### What It Means

`len()` returns the number of characters in a string.

### Syntax

```python
len(string)
```

### Example

```python
name = "Bhavana"
print(len(name))
```

Output:

```text
7
```

Example with a space:

```python
text = "Hello World"
print(len(text))
```

Output:

```text
11
```

The space between `Hello` and `World` is also counted.

### Key Points

- `len()` counts characters.
- Spaces are also counted.
- `len()` does not count words.
- It is commonly used with strings, lists, and other collections.

### Common Mistakes

#### Mistake 1: Thinking Spaces Are Ignored

```python
text = "Hi Bhavana"
print(len(text))
```

The space is counted.

#### Mistake 2: Thinking `len()` Counts Words

```python
sentence = "Python is easy"
print(len(sentence))
```

This counts characters, not words.

### Practice

Check the length of your full name and a sentence.

---

## 16. Checking Strings with `in` and `not in`

### What It Means

- `in` checks whether text exists inside another string.
- `not in` checks whether text does not exist inside another string.

### Syntax

```python
"text" in variable
"text" not in variable
```

### Example

```python
sentence = "Python is easy"

print("Python" in sentence)
print("Java" in sentence)
print("Java" not in sentence)
```

Output:

```text
True
False
True
```

### Case-Sensitive Example

```python
sentence = "Python is easy"

print("Python" in sentence)
print("python" in sentence)
```

Output:

```text
True
False
```

`Python` and `python` are different.

### Code Snippet

```python
email = "bhavana@gmail.com"

print("@gmail.com" in email)
print("@yahoo.com" in email)
print("@yahoo.com" not in email)
```

### Key Points

- The result is always `True` or `False`.
- String checks are case-sensitive.
- These checks are useful for emails, keywords, company names, and messages.

### Common Mistakes

#### Mistake 1: Ignoring Case Sensitivity

```python
email = "BHAVANA@GMAIL.COM"
print("@gmail.com" in email)
```

Output:

```text
False
```

Better:

```python
email = "BHAVANA@GMAIL.COM"
email = email.lower()
print("@gmail.com" in email)
```

### Practice

Check whether an email contains a domain and whether a sentence contains a keyword.

---

## 17. String Slicing

### What It Means

**Slicing** means taking a part of a string.

### Syntax

```python
string[start:end]
```

Important rule:

- The start index is included.
- The end index is excluded.

### Example

```python
text = "Hello, World!"
print(text[2:5])
```

Output:

```text
llo
```

It takes indexes `2`, `3`, and `4`. It does not include index `5`.

### Slice from the Start

```python
text = "Hello, World!"
print(text[:5])
```

Output:

```text
Hello
```

### Slice to the End

```python
text = "Hello, World!"
print(text[7:])
```

Output:

```text
World!
```

### Negative Slicing

```python
text = "Hello, World!"
print(text[-6:-1])
```

Output:

```text
World
```

### Code Snippet

```python
text = "Python Programming"

print(text[0:6])   # Python
print(text[7:])    # Programming
print(text[:6])    # Python
print(text[-11:])  # Programming
```

### Key Points

- Slicing takes a part of the string.
- The end index is not included.
- An empty start means start from the beginning.
- An empty end means continue to the end.
- Negative slicing counts from the end.

### Common Mistakes

#### Mistake 1: Thinking the End Index Is Included

```python
text = "Python"
print(text[0:3])
```

Output:

```text
Pyt
```

Not `Pyth`.

#### Mistake 2: Getting Confused by Negative Slicing

Use positive slicing first and learn negative slicing slowly.

### Practice

Slice `"Python Programming"` into different parts.

---

## 18. Modifying Strings

### What It Means

**String methods** are built-in actions you can perform on strings.

Important methods:

- `upper()`
- `lower()`
- `strip()`
- `replace()`
- `split()`
- `title()`
- `capitalize()`

### General Syntax

```python
string.method()
```

Examples:

```python
name.upper()
email.lower()
company.strip()
message.replace("Java", "Python")
data.split(",")
name.title()
```

### `upper()`

Converts a string to uppercase.

```python
name = "bhavana"
print(name.upper())
```

Output:

```text
BHAVANA
```

### `lower()`

Converts a string to lowercase.

```python
email = "BHAVANA@GMAIL.COM"
print(email.lower())
```

Output:

```text
bhavana@gmail.com
```

### `strip()`

Removes spaces from the beginning and end.

```python
company = " sharp india "
print(company.strip())
```

Output:

```text
sharp india
```

`strip()` does not remove spaces in the middle.

### `replace()`

Replaces one part of a string with another.

```python
message = "I am learning Java"
print(message.replace("Java", "Python"))
```

Output:

```text
I am learning Python
```

### `split()`

Splits a string into a list.

```python
data = "apple,banana,cherry"
print(data.split(","))
```

Output:

```text
['apple', 'banana', 'cherry']
```

### `title()`

Converts the first letter of every word to uppercase.

```python
name = "bhavana chintala"
print(name.title())
```

Output:

```text
Bhavana Chintala
```

### `capitalize()`

Converts the first character to uppercase and the rest to lowercase.

```python
text = "python is EASY"
print(text.capitalize())
```

Output:

```text
Python is easy
```

### Important Rule: String Methods Return a New Value

Wrong expectation:

```python
name = "bhavana"
name.upper()
print(name)
```

Output:

```text
bhavana
```

Correct:

```python
name = "bhavana"
name = name.upper()
print(name)
```

Output:

```text
BHAVANA
```

### Full Code Snippet

```python
company = " sharp india pvt ltd "
company = company.strip()
company = company.title()
print(company)

email = "BHAVANA@GMAIL.COM"
email = email.lower()
print(email)

message = "I am learning Java"
message = message.replace("Java", "Python")
print(message)

data = "apple,banana,cherry"
print(data.split(","))
```

### Key Points

- `upper()` makes text uppercase.
- `lower()` makes text lowercase.
- `strip()` removes beginning and ending spaces.
- `replace()` replaces text.
- `split()` breaks a string into parts.
- `title()` is useful for names and company names.
- String methods do not change the original string unless you store the result again.

### Common Mistakes

#### Mistake 1: Not Storing the Changed String

Wrong:

```python
company = " sharp india "
company.strip()
company.title()
print(company)
```

Correct:

```python
company = " sharp india "
company = company.strip()
company = company.title()
print(company)
```

Output:

```text
Sharp India
```

#### Mistake 2: Thinking `strip()` Removes All Spaces

```python
company = "Sharp India"
print(company.strip())
```

Output:

```text
Sharp India
```

The middle space remains.

### Practice

Clean names, company names, and email addresses.

---

## 19. String Concatenation

### What It Means

**Concatenation** means joining strings.

### Syntax

```python
string1 + string2
```

### Example

```python
first_name = "Bhavana"
last_name = "Chintala"

full_name = first_name + last_name
print(full_name)
```

Output:

```text
BhavanaChintala
```

There is no space because no space was added.

Correct:

```python
first_name = "Bhavana"
last_name = "Chintala"

full_name = first_name + " " + last_name
print(full_name)
```

Output:

```text
Bhavana Chintala
```

### Key Points

- `+` joins strings.
- Add spaces manually when needed.
- A string and number cannot be directly concatenated.
- F-strings are better for combining text and variables.

### Common Mistakes

#### Mistake 1: Forgetting the Space

Wrong:

```python
print(first_name + last_name)
```

Correct:

```python
print(first_name + " " + last_name)
```

#### Mistake 2: Concatenating a String and Number

Wrong:

```python
age = 25
print("Age: " + age)
```

Correct:

```python
age = 25
print("Age: " + str(age))
```

Better:

```python
age = 25
print(f"Age: {age}")
```

### Practice

Join a first name and last name with a space.

---

## 20. String Formatting

### What It Means

**String formatting** means inserting variables or values inside a string.

The preferred method is an **f-string**.

### Syntax

```python
f"text {variable}"
```

Formatting a number to two decimal places:

```python
f"{value:.2f}"
```

### Example

```python
name = "Bhavana"
age = 25

print(f"My name is {name} and my age is {age}")
```

### Why F-Strings Are Important

This gives an error:

```python
age = 25
print("My age is " + age)
```

This works:

```python
age = 25
print(f"My age is {age}")
```

### Formatting Decimal Places

```python
reply_rate = 12.3456
print(f"Reply rate: {reply_rate:.2f}%")
```

Output:

```text
Reply rate: 12.35%
```

### Full Code Snippet

```python
name = "Bhavana"
city = "Hyderabad"
lead_count = 100
reply_count = 12
reply_rate = reply_count / lead_count * 100

print(f"My name is {name}")
print(f"I am from {city}")
print(f"Out of {lead_count} leads, {reply_count} replied.")
print(f"Reply rate: {reply_rate:.2f}%")
```

### Key Points

- Use f-strings for clean output.
- Put variables inside `{}`.
- Use `:.2f` for two decimal places.
- F-strings are useful for reports, summaries, messages, and calculations.

### Common Mistakes

#### Mistake 1: Forgetting `f`

Wrong:

```python
name = "Bhavana"
print("My name is {name}")
```

Output:

```text
My name is {name}
```

Correct:

```python
name = "Bhavana"
print(f"My name is {name}")
```

#### Mistake 2: Using the Wrong Decimal Format

Correct:

```python
print(f"Reply rate: {reply_rate:.2f}%")
```

Wrong:

```text
print(f"Reply rate: {reply_rate.2f}%")
```

### Practice

Print clean reports using f-strings.

---

## 21. Escape Characters

### What It Means

An **escape character** is a backslash `\` used to insert special characters inside a string.

### Important Escape Characters

| Escape character | Meaning |
|---|---|
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |
| `\n` | New line |
| `\t` | Tab space |

### Double Quote Inside Double Quotes

```python
text = "She said \"Python is easy\""
print(text)
```

Output:

```text
She said "Python is easy"
```

### New Line

```python
print("Name: Bhavana\nGoal: Learn Python")
```

Output:

```text
Name: Bhavana
Goal: Learn Python
```

### Tab Space

```python
print("Name:\tBhavana")
print("City:\tHyderabad")
```

Output:

```text
Name:   Bhavana
City:   Hyderabad
```

### Full Code Snippet

```python
print("She said \"Python is easy\"")
print("Name: Bhavana\nGoal: Learn Python\nDay: 1")
print("Name:\tBhavana")
print("City:\tHyderabad")
print("Goal:\tPython")
```

### Key Points

- Use escape characters when normal quotes confuse Python.
- `\n` moves to a new line.
- `\t` adds tab space.
- Use `\"` when you want double quotes inside a double-quoted string.

### Common Mistakes

#### Mistake 1: Not Escaping Inner Quotes

Wrong:

```text
print("She said "Hello"")
```

Correct:

```python
print("She said \"Hello\"")
```

### Practice

Print quotes, new lines, and tab spaces.

---

## 22. Important String Methods to Learn First

Do not try to memorize every string method in one day. Learn and practice the most useful methods first.

### Method Reference

| Method | Meaning | Example |
|---|---|---|
| `upper()` | Converts to uppercase | `"hi".upper()` |
| `lower()` | Converts to lowercase | `"HI".lower()` |
| `strip()` | Removes beginning and ending spaces | `" hi ".strip()` |
| `replace()` | Replaces text | `"Java".replace("Java", "Python")` |
| `split()` | Splits a string into a list | `"a,b".split(",")` |
| `title()` | Converts to title case | `"hello world".title()` |
| `capitalize()` | Capitalizes the first character | `"hello".capitalize()` |
| `count()` | Counts occurrences | `"banana".count("a")` |
| `find()` | Finds a position | `"hello".find("e")` |
| `startswith()` | Checks the beginning | `"hello".startswith("he")` |
| `endswith()` | Checks the ending | `"test.py".endswith(".py")` |
| `isdigit()` | Checks whether all characters are digits | `"123".isdigit()` |
| `isalpha()` | Checks whether all characters are alphabets | `"abc".isalpha()` |

### Example

```python
text = " python programming "

print(text.strip())
print(text.upper())
print(text.lower())
print(text.title())
print(text.count("p"))
print(text.find("programming"))
print(text.strip().startswith("python"))
print(text.strip().endswith("programming"))

number = "123"
print(number.isdigit())

word = "Bhavana"
print(word.isalpha())
```

### Key Points

- Learn the most useful string methods first.
- Practice methods using real text values.
- `strip()`, `lower()`, and `title()` are useful for cleaning user input, names, emails, and company names.

### Common Mistakes

- Do not try to memorize every string method in one day.
- Do not forget that string methods return a new value.
- Store the changed value if you want to use it later.

### Practice

Apply every method in the table at least once.

---

## 23. One Master Revision Code Snippet

Create a file named `day1_revision.py` and use it as your complete Day 1 revision code.

```python
# Day 01 Revision: Python Basics, Variables, Data Types, Numbers,
# Casting, and Strings

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
```

### Concepts Revised by This File

- Output
- Comments
- Variables
- Variable names
- Multiple assignment
- Data types
- Numbers
- Casting
- Strings
- Indexing
- Slicing
- String checking
- String methods
- F-strings
- Escape characters

### Important Practice Instructions

- Do not only read this code.
- Type it yourself.
- Run it.
- Check the output line by line.
- Modify values and observe what changes.

Use this file as your complete Day 1 revision practice.

---

## 24. Must-Know Interview Questions from Day 1

### Python Basics

1. What is Python?
2. Who created Python?
3. What is Python used for?
4. What is the extension of a Python file?
5. What is an interpreter?
6. What is `print()` used for?
7. Does Python need semicolons?
8. Why is indentation important in Python?

### Variables

9. What is a variable?
10. Do we need to declare a variable's type in Python?
11. What does dynamically typed mean?
12. Can a variable change its type in Python?
13. Are variable names case-sensitive?
14. What are valid and invalid variable names?
15. What naming style is preferred in Python?

### Output Variables

16. What is the difference between `print(x, y)` and `print(x + y)`?
17. What happens when you do `"10" + "20"`?
18. What happens when you do `10 + 20`?
19. Why does `"Age is " + age` give an error when `age` is an integer?

### Data Types and Numbers

20. What is a data type?
21. What is the difference between `int` and `float`?
22. What does `type()` do?
23. What is the output of `type("100")`?
24. What is the output of `type(100)`?
25. What are Python's numeric types?
26. What is the result of `20 / 10`?

### Casting

27. What is casting?
28. What does `int("100")` do?
29. What does `float("3.5")` do?
30. What does `str(25)` do?
31. What is the output of `int(4.9)`?
32. Why does `int("3.5")` give an error?

### Strings

33. What is a string?
34. Are single quotes and double quotes both allowed?
35. What is a multiline string?
36. What is string indexing?
37. What is the first index in Python?
38. What is negative indexing?
39. What does `len()` do?
40. What is slicing?
41. Is the end index included in slicing?
42. What does `strip()` do?
43. What does `upper()` do?
44. What does `lower()` do?
45. What does `replace()` do?
46. What does `split()` return?
47. What is string concatenation?
48. What is an f-string?
49. What does `:.2f` do?
50. What is an escape character?

---

## 25. Practice Problems and Use Cases

### A. Basic Output and Comments

1. Print your name, city, and goal.
2. Print five calculations using `+`, `-`, `*`, and `/`.
3. Print `"10 + 20"` and `10 + 20`, then explain the difference.
4. Write a program with three useful comments.

### B. Variables

5. Create variables for `name`, `age`, `city`, and `goal`.
6. Create variables for `company_name`, `industry`, and `location`.
7. Create variables for `lead_count`, `reply_count`, and `meeting_count`.
8. Print all variables using clear labels.

### C. Variable Names

9. Write five valid variable names.
10. Write five invalid variable names and explain why they are invalid.
11. Convert the following into proper Python variable names:

```text
company name
lead-count
1reply
Meeting Count
customer email
```

Expected style:

```text
company_name
lead_count
reply1
meeting_count
customer_email
```

### D. Multiple Assignment

12. Assign a name, city, and goal in one line.
13. Assign `"Pending"` to three status variables in one line.
14. Unpack three values from a list into three variables.

### E. Data Types

15. Create one variable each for `str`, `int`, `float`, `bool`, and `NoneType`.
16. Print the type of each variable.
17. Create `"100"` and `100`, print their types, and explain the difference.

### F. Numbers and Casting

18. Convert `"100"` to an integer and add `50`.
19. Convert `3` to a float.
20. Convert `25` to a string.
21. Check the output of `int(2.8)`.
22. Check the output of `float("4.5")`.
23. Try `int("3.5")` and understand the error.

### G. String Basics

24. Store your full name in a variable.
25. Print the first character.
26. Print the last character.
27. Print the length of your full name.
28. Convert your name to uppercase.
29. Convert your name to lowercase.
30. Convert your name to title case.

### H. String Slicing

31. Given:

```python
text = "Python Programming"
```

Print:

```text
Python
Programming
Pyth
gram
```

32. Print the first five characters of your full name.
33. Print the last five characters of your full name.

### I. String Modification

34. Clean this company name:

```python
company = " sharp india pvt ltd "
```

Expected output:

```text
Sharp India Pvt Ltd
```

35. Convert this email to lowercase:

```python
email = "BHAVANA@GMAIL.COM"
```

36. Replace `"Java"` with `"Python"`:

```python
message = "I am learning Java"
```

37. Split this data:

```python
data = "apple,banana,cherry"
```

### J. String Checking

38. Check whether an email contains `"@gmail.com"`.
39. Check whether a sentence contains `"Python"`.
40. Check whether `"Java"` is not present in a sentence.
41. Check whether a file name ends with `.py`.

Example:

```python
file_name = "practice.py"
print(file_name.endswith(".py"))
```

### K. Concatenation and Formatting

42. Join a first name and last name with a space.
43. Print your name, age, and city using an f-string.
44. Print:

```text
Out of 100 leads, 12 replied.
```

45. Print a reply rate with two decimal places.

### L. Escape Characters

46. Print:

```text
She said "Python is easy"
```

47. Print the following using `\n`:

```text
Name: Bhavana
Goal: Learn Python
Day: 1
```

48. Print the following using `\t`:

```text
Name    Bhavana
City    Hyderabad
Goal    Python
```

---

## 26. Mini Projects for Full Understanding

### Mini Project 1: Personal Profile Report

#### Objective

Create a small personal profile report by cleaning and formatting text values.

#### Starting Values

```python
name = " Bhavana Chintala "
city = "hyderabad"
goal = "python job preparation"
email = "BHAVANA@GMAIL.COM"
```

#### Expected Output

```text
Name: Bhavana Chintala
City: Hyderabad
Goal: Python Job Preparation
Email: bhavana@gmail.com
```

#### Concepts Used

- Variables
- Strings
- `strip()`
- `title()`
- `lower()`
- F-strings

#### Common Mistakes

- Do not forget to store the cleaned values.
- Remember that `strip()`, `title()`, and `lower()` return new values.

#### Practice

Build this project in a separate `.py` file and run it.

### Mini Project 2: Lead Reply Report

#### Objective

Create a small report using lead, reply, and meeting counts.

#### Starting Values

```python
lead_count = 100
reply_count = 12
meeting_count = 3
```

#### Required Output

```text
Total leads: 100
Replies: 12
Meetings: 3
Reply rate: 12.00%
Meeting rate: 3.00%
```

#### Concepts Used

- Variables
- Numbers
- Division
- F-strings
- `:.2f`

#### Common Mistakes

- Multiply by `100` when calculating a percentage.
- Use `:.2f` for two decimal places.

#### Practice

Build this project and change the lead, reply, and meeting values.

### Mini Project 3: Company Name Cleaner

#### Objective

Clean a company name and print basic string details.

#### Starting Value

```python
company = " sharp india pvt ltd "
```

#### Expected Output

```text
Original company: sharp india pvt ltd
Clean company: Sharp India Pvt Ltd
First character: S
Last character: d
Length: 19
```

#### Concepts Used

- `strip()`
- `title()`
- Indexing
- `len()`
- F-strings

#### Common Mistakes

- Do not check the first and last characters before cleaning when the output expects the cleaned company.
- Remember that spaces affect indexing and length.

#### Practice

Build this project and try it with another company name.

### Mini Project 4: Email Checker

#### Objective

Clean an email address and check whether it contains the expected parts.

#### Starting Value

```python
email = "BHAVANA@GMAIL.COM"
```

#### Expected Output

```text
Clean email: bhavana@gmail.com
Contains gmail: True
Ends with .com: True
```

#### Concepts Used

- `lower()`
- `in`
- `endswith()`
- F-strings

#### Common Mistakes

- String checks are case-sensitive.
- Convert the email to lowercase before checking for lowercase text such as `"@gmail.com"`.

#### Practice

Build this project and try it with another email provider.

---

## 27. Final Day 1 Checklist

Before moving ahead, you should be able to do the following without looking at the notes:

- [ ] Create and run a `.py` file without help.
- [ ] Use `print()` correctly.
- [ ] Write useful comments in Python.
- [ ] Create variables.
- [ ] Use correct variable names.
- [ ] Use multiple assignment.
- [ ] Print variables clearly.
- [ ] Understand `str`, `int`, `float`, `bool`, and `None`.
- [ ] Use `type()` to check a variable's data type.
- [ ] Use `int()`, `float()`, and `str()`.
- [ ] Explain the difference between `100` and `"100"`.
- [ ] Use basic arithmetic operators.
- [ ] Create strings.
- [ ] Use string indexing.
- [ ] Use negative indexing.
- [ ] Use `len()`.
- [ ] Use slicing.
- [ ] Use `upper()`, `lower()`, `strip()`, `replace()`, `split()`, and `title()`.
- [ ] Use `in` and `not in`.
- [ ] Join strings.
- [ ] Use f-strings.
- [ ] Use `:.2f` for two decimal places.
- [ ] Use escape characters.

## Next Task

Create a file named `day1_full_revision_practice.py` and solve at least **25 practice problems** from the list above.
