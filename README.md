# 🐍 Python Notes

This document provides a concise overview of basic Python concepts, useful as a quick reference or beginner guide.

---

## 📦 Data Types

| Data Type | Description                          | Examples                     |
| --------- | ------------------------------------ | ---------------------------- |
| `int`     | Integer numbers                      | `3`, `300`, `200`            |
| `float`   | Decimal numbers                      | `2.3`, `4.6`, `100.0`        |
| `str`     | Text / characters                    | `"hello"`, `"200"`           |
| `list`    | Ordered, mutable collection          | `[10, "hello", 200.3]`       |
| `dict`    | Key-value pairs                      | `{ "k1": "v1", "k2": "v2" }` |
| `tuple`   | Ordered, immutable collection        | `(10, "hello", 200.3)`       |
| `set`     | Unordered collection of unique items | `{ "v1", "v2" }`             |
| `bool`    | Boolean values                       | `True`, `False`              |

---

## 🏷️ Variables

### Rules

1. Variable names **cannot start with a number**.
2. Spaces and special characters like `@ # $ "` are **not allowed**.
3. As per **PEP8 best practices**, variable names should be **lowercase**.
4. Python supports **dynamic typing**, so reassignment with a different type is valid:

```python
my_var = 1
my_var = "hello"
```

5. To check the data type of a variable, use the `type()` function:

```python
type(my_var)
```

6. It is allowed to use variable names that match built-in types, **but not recommended**:

```python
int = "hello"
str = 10
```

---

## 🔤 Strings

1. Strings can be defined using **single** or **double quotes**:

```python
"hello"
'hello'
```

2. Strings are **index-based**:

```text
"hello"
Character:  h   e   l   l   o
Index:      0   1   2   3   4
Rev Index: -5  -4  -3  -2  -1
```

3. **String Slicing** allows extracting substrings using the syntax:

```text
[start : stop : step]
```

* `start`: starting index (inclusive)
* `stop`: ending index (exclusive)
* `step`: jump size

```text
Example:
val = "hello world"
val[6:11]: world
val[-1]: d
val[6:11:2]: wrd
reverse of val[::-1]: dlrow olleh
length of val: 11
val[1::-1]: eh
```

4. New line character `\n`:

```python
print('hello \n world')
```

Output:

```text
hello
world
```

5. Tab character `\t`:

```python
print('hello \t world')
```

Output:

```text
hello	world
```

6. To get the total number of characters in a string, use `len()`:

```python
len('i am')
```

7. String are immutable and hence val[0]="hello" not allowed

8. Just like java string can be concatenated, but here only with string.
```python
x = "hello"
x = x+ " world"
print(x) # hello world
letter = "z"
letter = letter * 5
print(letter) # zzzzz
x = "10"
x=x+1
print(x) # error string can be concatenated with string only.
```

9. String methods like x.upper(), x.lower(), x.split() 
```python
# split default delimeter is space
x.split()
x.split(" ")
x.split("i")
```

10. print Formatting in string
```python
# Example using format method of str
x = 'Hello my name is {} and i am {}'.format('kush','engineer')
x = 'the {2} {1} {0}'.format('fox','brown','quick')  # the quick brown fox 
x = 'the {q} {b} {f}'.format(q='quick',b='brown',f='fox')  # the quick brown fox
x = 'the {f} {f} {f}'.format(q='quick',b='brown',f='fox')  # the fox fox fox
x = 'the {1} {1} {1}'.format('quick','brown','fox') # the brown brown brown
# Float formatting syntax is string:width.precisionf
result = 100/777
print(f"result: {result}") # print result: 0.1287001287001287
print(f"result: {result:.3f}") # print result: 0.129 (default width is 1)
print(f"result: {result:10.5f}") # print result:      0.12870 (width is 10 and hence 10 spaces)
# Example using String interpolation using f"" syntax introduced in python 3.6
name = "John"
age = 30
print(f"name: {name} and age: {age}.") # print name: John and age: 30.
print(f"name: {name.upper()} and age: {age + 5} and marks: {result:.3f}.") # print name: JOHN and age: 35 and marks: 0.129.
```

---

## 🔤 Lists
they are ordered collection. Some useful list function example are->
```python
my_list = [100,"hello",23.45,True]
print(f"my_list: {my_list}") # print my_list: [100, 'hello', 23.45, True]
print(f"my_list[0]: {my_list[0]}") # print my_list[0]: 100
print(f"my_list[1][0]: {my_list[1][0]}") # print my_list[1][0]: h
print(f"my_list[1:3]: {my_list[1:3]}") # print my_list[1:3]: ['hello', 23.45]
print(f"my_list[::-1]: {my_list[::-1]}") # print my_list[::-1]: [True, 23.45, 'hello', 100]
print(f"length of my_list: {len(my_list)}") # print length of my_list: 4
another_list = [200, "world"] 
combined_list = my_list + another_list
print(f"combined_list: {combined_list}") # print combined_list: [100, 'hello', 23.45, True, 200, 'world']
my_list[0] = 500
print(f"modified my_list: {my_list}") # print modified my_list: [500, 'hello', 23.45, True]
my_list.append("new item")
print(f"my_list after append: {my_list}") # print my_list after append: [500, 'hello', 23.45, True, 'new item']
print(f"item popped from my_list: {my_list.pop()}") # print item popped from my_list: new item
print(f"my_list after pop: {my_list}") # print my_list after pop: [500, 'hello', 23.45, True]
print(f"item popped from my_list at index 1: {my_list.pop(1)}") # print item popped from my_list at index 1: hello
print(f"my_list after pop at index 1: {my_list}") # print my_list after pop at index 1: [500, 23.45, True]
my_list.remove(500)
print(f"my_list after remove: {my_list}") # print my_list after remove: [23.45, True]
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort()
print(f"sorted num_list: {num_list}") # print sorted num_list: [1, 2, 5, 5, 6, 9]
num_list.reverse()
print(f"reversed num_list: {num_list}") # print reversed num_list: [9, 6, 5, 5, 2, 1]
```