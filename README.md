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