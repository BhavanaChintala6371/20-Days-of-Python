# Day 02 - Python Booleans, Operators, and Collections

This folder contains the Day 02 revision material from the 1-Week Python Job Preparation Plan.

Day 02 moves from individual values into decision-making and collection-based programming. The main areas are Boolean logic, Python operators, and the core collection types: lists, tuples, sets, frozensets, and dictionaries.

---

## Learning Objectives

After completing this day, you should be able to:

- work with `True`, `False`, truthy values, and falsy values
- write Boolean-returning expressions and functions
- check data types with `isinstance()`
- use arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators
- understand operator precedence and use parentheses clearly
- create and manage lists
- use indexing, slicing, loops, list comprehensions, sorting, copying, and joining
- create and work with immutable tuples
- use tuple packing, unpacking, joining, and repetition
- create sets and perform set comparisons
- understand `frozenset`
- create, access, update, remove, copy, and loop through dictionaries
- create and process nested dictionaries

---

## Topics Covered

### Booleans

- Python Boolean values
- Boolean expressions and conditions
- `bool()`
- truthy and falsy values
- functions returning Booleans
- `isinstance()`
- common Boolean mistakes

### Operators

- arithmetic operators
- assignment operators
- walrus operator awareness
- ternary expressions
- comparison operators
- chained comparisons
- logical operators and short-circuiting
- identity operators
- membership operators
- bitwise operators
- operator precedence

### Lists

- list creation and properties
- positive and negative indexing
- slicing and membership
- changing items and ranges
- `append()`, `insert()`, and `extend()`
- `remove()`, `pop()`, `del`, and `clear()`
- direct, indexed, and `while` loops
- list comprehension
- sorting and reversing
- independent copies
- joining lists
- important list methods

### Tuples

- tuple creation and properties
- one-item tuples
- indexing, slicing, and membership
- tuple update workarounds
- packing and unpacking
- starred unpacking
- tuple loops
- joining and repeating tuples
- `count()` and `index()`

### Sets and Frozenset

- set creation and properties
- duplicate removal
- empty sets
- membership and loops
- `add()` and `update()`
- `remove()`, `discard()`, `pop()`, `clear()`, and `del`
- union, intersection, difference, and symmetric difference
- update-style set operations
- `frozenset`
- important comparison methods

### Dictionaries

- key-value pairs
- dictionary creation and duplicate keys
- square-bracket access and `get()`
- `keys()`, `values()`, and `items()`
- changing and adding items
- `pop()`, `popitem()`, `del`, and `clear()`
- looping through keys, values, and pairs
- correct dictionary copying
- nested dictionaries
- important dictionary methods

---

## Suggested Folder Contents

```text
week_01/
└── day_02_basics/
    ├── README.md
    ├── notes.md
    ├── day2_part1_part2_revision.py
    ├── day2_part1_part2_full_revision_practice.py
    ├── age_eligibility_checker.py
    ├── even_or_odd_checker.py
    ├── time_converter.py
    ├── todo_list_manager.py
    ├── marks_analyzer.py
    ├── unique_skills_tracker.py
    ├── student_profile_dictionary.py
    ├── contact_book.py
    └── simple_shopping_cart.py
```

The mini-project filenames above are clear names for organizing the nine projects included in the Day 02 material.

---

## Main Revision Files

### `notes.md`

Contains the complete organized Day 02 revision notes, including:

- definitions
- syntax
- code examples
- key points
- common mistakes
- the master revision program
- 139 practice problems
- 9 mini projects
- 148 interview questions
- the final completion checklist

### `day2_part1_part2_revision.py`

A combined revision program for:

- Booleans
- operators
- lists
- tuples
- sets
- frozenset
- dictionaries

Type the program yourself, run it section by section, and change values to observe the results.

### `day2_part1_part2_full_revision_practice.py`

Use this file to solve at least 60 of the 139 Day 02 practice problems.

---

## Mini Projects

1. **Age Eligibility Checker** - Boolean logic, comparisons, logical operators, and ternary expression
2. **Even or Odd Checker** - modulus, comparison, and ternary expression
3. **Time Converter** - floor division, modulus, arithmetic, and formatted output
4. **To-Do List Manager** - common list operations, membership, and loops
5. **Marks Analyzer** - sorting, totals, averages, highest and lowest marks
6. **Unique Skills Tracker** - set updates and group comparison operations
7. **Student Profile Dictionary** - dictionary creation, updates, access, and loops
8. **Contact Book** - nested dictionaries and nested loops
9. **Simple Shopping Cart** - list of dictionaries, loops, arithmetic, and running totals

---

## Recommended Study Order

1. Read the Boolean and operator sections in `notes.md`.
2. Type and run the related examples.
3. Study lists carefully because they are used frequently in later Python topics.
4. Compare lists, tuples, sets, frozensets, and dictionaries.
5. Type the complete master revision code.
6. Solve the practice problems without copying the answers.
7. Complete the nine mini projects one at a time.
8. Review the interview questions aloud.
9. Use the final checklist before moving to Day 03.

---

## Running a Python File

From the terminal inside this folder:

```bash
python filename.py
```

On systems using the Python launcher:

```bash
py filename.py
```

A successful run normally ends without a traceback. Always inspect the output and confirm that it matches the expected logic.

---

## Core Collection Comparison

| Collection | Ordered | Changeable | Duplicates | Access |
|---|---:|---:|---:|---|
| List | Yes | Yes | Yes | Index |
| Tuple | Yes | No | Yes | Index |
| Set | No | Add/remove only | No | Loop or membership |
| Frozenset | No | No | No | Loop or membership |
| Dictionary | Yes | Yes | No duplicate keys | Key |

---

## Important Rules to Remember

- `True`, `False`, and `None` begin with capital letters.
- `=` assigns; `==` compares.
- `/` returns a float; `//` performs floor division.
- `%` returns a remainder.
- `and`, `or`, and `not` are logical operators.
- `==` checks equal values; `is` checks the same object.
- List and tuple indexing begins at `0`.
- Slicing includes the start and excludes the end.
- Lists are mutable; tuples are immutable.
- Sets remove duplicates and do not support indexing.
- `{}` creates an empty dictionary; `set()` creates an empty set.
- Dictionary `in` checks keys by default.
- Use `copy()` when an independent list or dictionary copy is required.

---

## Completion Checklist

- [ ] Read the complete `notes.md` file.
- [ ] Type and run `day2_part1_part2_revision.py`.
- [ ] Solve at least 60 practice problems.
- [ ] Complete all 9 mini projects.
- [ ] Review all interview questions.
- [ ] Confirm the final Day 02 checklist without looking at the notes.

---

## Day 02 Outcome

By the end of Day 02, you should be able to make decisions with Boolean logic and operators, choose the correct collection type, and perform common operations on lists, tuples, sets, frozensets, and dictionaries.
