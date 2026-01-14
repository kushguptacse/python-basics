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

## 🔤 Arithmetic operation rule
1. if any number is float result is float.

2. result of division always float. example - 10/2 = 5.0

3. power can be calculated using ** . example - 2**3 = 8

4. sqrt can be calculated using x**0.5
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
sample = ['a','a','b']
print(f"count 'a': {sample.count('a')}") # print 2
```
---

## 🔤 Dictionaries
1. They are java varient of hashmap. Some useful functions example are->
```python
sample = {'name':'kush','age':34,'k2':[1,2,3], 'k3':{'nested':900}}
print(sample['name']) # print kush
print(sample['k2'][1]) # print 2
print(sample['k3']['nested']) # print 900
sample['name']='agent'
print(sample['name']) # print agent
sample[2351]='kk'
print(sample) # print {'name': 'agent', 'age': 34, 'k2': [1, 2, 3], 'k3': {'nested': 900}, 2351: 'kk'}
```

2. Allowed keys in dict are immutable objects like int, float, str, tuple, bool, frozenset. We can also mix key types
```python
data = {1: "int key", "1": "string key"}
print(data[1])    # int key
print(data["1"])  # string key
```

3. If you want to maintain order of dict keys just like LinkedHashMap python has ordereddict

---

## 🔤 Tuples
1. They are just like list but are immutable where list are not. means we cannot even change the value present at specific index after creation. Some useful functions example are->
```python
sample = (1,2,3)
print(sample) # print (1,2,3)
print(sample[0]) # print 1
print(sample[:2]) # print (1,2)
```

2. Tuple has only 2 methods  e.g. count(), index().
```python
sample = ('a','a','b')
print(len(sample)) # print 3 (This is build in method. not provided by tuple)
print(sample.count('a')) # print 2
print(sample.index('a')) # print 0
```

3. Tuple are immutable but not nested immutable.
```python
sample = ('k',[1,2],9.1) # valid, tuple allows dict and all type as value
sample[0]= 'hello' # it will give error. not allowed
sample[1][1] = 44
print(sample) # print ('k', [1, 44], 9.1)
```
---

## 🔤 Sets
1. They are just like HashSet. It's constructor can take list,tuple,str and any iterable. examples of declartion:
```python
myset= set()
myset.add('hello') # only list has append not set and only set has add not list.
print(myset) # print {'hello'}
myset = set("hello")
print(myset)   # {'h', 'e', 'l', 'o'}
myset = set([1,2,3,4])
print(myset) # print {1,2,3,4}
myset = set((1,2,3))
print(myset)# print {1,2,3}
myset = {1,2,3}
print(myset)# print {1,2,3}
myset = {1,2,3,2}
print(myset)# print {1,2,3}
myset = {} # valid, but it will create empty dict not set.
```
---

## 🔤 bool
valid value True or False. all comparison operator returns bool value
```python
val = False
print(val)
print(type(val)) # print <class 'bool'>
val = None
print(val) # print None
print(type(val)) # print <class 'NoneType'>
```
---

## 🔤 file io
1. open, close and read file operations 
```python
myfile = open('myfile.txt') # complete path can be given
content = myfile.read() 
print(content) # prints file entire content wiht line seprated as \n
content = myfile.read()
print(content) # prints nothing as file pointer is at the end of file
myfile.seek(0) # move file pointer to start of the file
content = myfile.read()
print(content) # prints file entire content again
myfile.seek(0)
lines = myfile.readlines() # return list where each line is new item in list.
print(lines) # prints ['hello this is txt file\n', 'first line\n', 'second line']
myfile.close() # if not closed it may lead to memory leak
```
2. To avoid closing file everytime, 'with' can be used. 
```python
with open('myfile.txt') as myfile2: # automatically closes the file after with block is executed
    content2 = myfile2.read()
print(content2) # prints file entire content
```

3. Different mode supported while opening file 'r','w','a','r+','w+'

| Mode | Access Type        | File Exists | File Does Not Exist | File Pointer Position |
|------|--------------------|-------------|----------------------|-----------------------|
| `r`  | Read only          | Opens file  | ❌ Error             | Beginning             |
| `w`  | Write only         | Overwrites  | Creates file         | Beginning             |
| `a`  | Append only        | Appends     | Creates file         | End                   |
| `r+` | Read & Write       | Opens file  | ❌ Error             | Beginning             |
| `w+` | Write & Read       | Overwrites  | Creates file         | Beginning             |


```python

with open('myfile.txt','r') as myfile2: # open file in read mode and is default mode
    content2 = myfile2.read()
    # myfile2.write('new line') # will give error as file is opened in read mode
print(content2) # prints file entire content

with open('myfile.txt','w') as myfile2: # open file in write mode and overwrites existing content
    myfile2.write('new line')
    # myfile2.read() # will give error as file is opened in write mode
```