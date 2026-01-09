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

