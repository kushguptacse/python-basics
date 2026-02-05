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
type(my_var) #<class 'str'>
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

5. to get division result in integer format use // . example - 9//5: 1
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

```python
Example:
val = "hello world"
val[7:11] #print orld
val[-1] #print d
val[7:11:2] #print ol
val[::-1] #print reverse i.e. dlrow olleh
val[1::-1]#print eh
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
len('i am') # print 4
```

7. String are immutable and hence val[0]="hello" not allowed

8. Just like java string can be concatenated using '+' operator, but here only with string.
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
# Float formatting syntax is variable:width.precisionf
result = 100/777
print(f"result: {result}") # print result: 0.1287001287001287
print(f"result: {result:.3f}") # print result: 0.129 (default width is 1)
print(f"result: {result:10.5f}") # print result:      0.12870 (width is 10 and hence 10 spaces)
print(f"{10.9:10.5f}") #print   10.90000
# Example using String interpolation using f"" syntax introduced in python 3.6
name = "John"
age = 30
print(f"name: {name} and age: {age}.") # print name: John and age: 30.
print(f"name: {name.upper()} and age: {age + 5} and marks: {result:.3f}.") # print name: JOHN and age: 35 and marks: 0.129.
```

11. join operator: is used to join list of strings with a delimeter (opposite of split)
```python
print(" ".join("hello world"))  # print h e l l o   w o r l d
print(" ".join(["hello","world","guys"]))  # print hello world guys
```

12. capitalize: if you want to capitalize only first char of string.
```python
print(f"capitalize method result of helloworld is : {'helloworld'.capitalize()}") # print Helloworld
```
---

## 🔤 Lists
they are ordered collection. and we use append method to add element to list. example ->
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
data = {1: "int", "1": "string"}
print(data[1])    # int key
print(data["1"])  # string key
```

3. If you want to maintain order of dict keys just like LinkedHashMap python has ordereddict. after python3.7+ dict maintains insertion order

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
print(len(sample)) # print 3 (This is built-in method. not provided by tuple class)
print(sample.count('a')) # print 2
print(sample.index('a')) # print 0
```

3. Tuple is immutable, but can contain mutable objects
```python
sample = ('k',[1,2],9.1) # valid, tuple allows dict and all type as value
sample[0]= 'hello' # it will give error. not allowed
sample[1][1] = 44
print(sample) # print ('k', [1, 44], 9.1)
```

```
---

## 🔤 Sets
1. They are just like HashSet. using add method element can be added. It's constructor can take list,tuple,str and any iterable. examples of declartion:
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

print(f"1<2 and 2<3: {1<2 and 2<3}")# print True.
print(f"1<2 or 2<3: {1<2 or 2>3}")# print True.
print(f"not 1==1: {not 1==1}")# print False.
print(f"1!=1: {1!=1}")# print False.
print(f"2!=2.0: {2!=2.0}") # print False
print(f"'2'==2: {'2'==2}") # print False
print(f"2==2.0: {2==2.0}") # print True as for float python just check value.
print(f"1<2<3: {1<2<3}")# print True. it is evaluated left to right
print(f"1<2>3: {1<2>3}")# print False. it is evaluated left to right
print(f"1<2 and 2<3: {1<2 and 2<3}")# print True.
print(f"1<2 or 2<3: {1<2 or 2>3}")# print True.
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
myfile.close() # if not closed it may lead to resource leak
```
2. To avoid closing file everytime, 'with' can be used. 
```python
with open('myfile.txt') as myfile2: # automatically closes the file after with block is executed
    content2 = myfile2.read() #all the blocks like with,if/else,for/while,try/except does not create new scope
print(content2) # prints file content. 
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
---

## 🔤 statements
1. if, elif and else syntax
```python
name = 'kush'
if name=='kush':
    print(f"name is {name}")
elif name == 'pizza':
    print(f"name is {name}")
else:
    print(f"name is {name}")
```
2. for loops: iterable objects can be used inside for loop. example - string, list, dictionary, tuple
```python
for item in [1, 2, 3]:
    if item % 2 == 0:
        print(f"item is even : {item}")

# iterate over string
for letter in "hello world":
    print(letter)

# iterate over tuple
for tup in (1,2,3):
    print(tup)

# iterate over list of tuple
for a,b in [(1,2),(3,4),(5,6)]:
    print(f"first tuple {a} and second tuple {b}")

# iterate over dictionary using keys
sample_dict = {"k1":"v1","k2":"v2","k3":"v3"}
for key in sample_dict:
    print(f"elements with key {key} is {sample_dict[key]}")

# iterate over dictionary using dictionary entry
for key,item in sample_dict.items(): #tuple
    print(f"elements with key {key} is {item}")
```

3. while loops: it has else also which get executed when loop condition finishes.
```python
x=0
while x<5:
    print(f"x is {x}")
    x+=1
else:
    print(f"x is {x} now") #print x is 5 now
```

4. pass, continue and break: pass is used to add as place holder, so that python wont give any error of empty loop/class etc.
```python
for it in [1,2,3]:
    pass # now this code wont execute, it is just to avoid python to give error of writing empty loop.
```

5. range operator: range(start,end,stepSize) where end index is not included
```python
for num in range(1, 11): #print numbers from 1 till 10
    print(num)

for num in range(0, 11, 2):  # print even numbers from 0 till 10 as step size is 2
    print(num)
```

6. enumerate operator: it converts iterable into tuple with index and value. so that we can iterate with index and value
```python
word = "abcde"

for i, val in enumerate(word): 
    print(f"item at index {i} is {val}")

nums = [1,2,35]
for i, val in enumerate(nums):
    print(f"item at index {i} is {val}")
```
7. zip operator: using zip you can iterate on multiple iterables together index wise. and loop will iterate till length of smallest iterable exhausted.
```python
l1 = [1,2,3]
l2 = ['a','b','c']
l3 = [1.1,2.2,3.3]

for x,y,z in zip(l1,l2,l3):
    print(f"{x},{y},{z}") # it print 1,a,1.1 in first line and then 2,b,2.2 and so on

l4=[False]
for x,y in zip(l1,l4):
    print(f"{x},{y}") # it print 1,False only. as zip iterate only to the lowest length iterable passed 
```
8. in operator: check if specific value is present in iterable
```python
if 1 in [1,2,3]:
    print("exists")

d={'k1':'v1',"k2":"v2"}
if "k1" in d:
    print("exists")

if "v1" in d.values():
    print("exists")

```
9. min, max operator: find min and max in iterable
```python
l1=[1,2,3]
print(f"min element in list is : {min(l1)}") # print 1
print(f"max element in list is : {max(l1)}") # print 3
```
10. input operator: to read value from console use input function. it return string value
```python
first = input('enter a number here: ')
print(int(first)) # input is read as str value.
```
11. random library: it has useful functions related to randomization
```python
from random import shuffle, randint
l = [1,2,3,4]
shuffle(l) #it shuffles the list l
print(l) #print [3,1,2,4]
var = randint(0,100)
print(var) #print 22
```

12. list comprehension: short-hand syntax to iterate iterable and assign back to list.
```python
print("list comprehension example")
sam_list = [1,2,3]
mylist = [item*2 for item in sam_list] # it will iterate through sam_list and assign double of each number to mylist
print(mylist) # print [2,4,6]
mylist = [item for item in 'word'] 
print(mylist) # print ['w', 'o', 'r', 'd']
mylist = [item**2 for item in range(0,11)] 
print(mylist) # print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
mylist = [item**2 for item in range(0,11) if item%2==0] 
print(mylist) # print [0, 4, 16, 36, 64, 100]
# we can also apply shorthand if else in list compreshension and also nested forloop. but it will make code less readable
```

13. Iterables (e.g. tuples, list, set etc) can be unpacked directly and assigned into variables.
```python
coord=(2,5)
x,y=coord #x=2,y=5
a,b={1,2} # a=1,b=2
l1,l2 = [1,2,3] # it will give error as three variables required
f,*s=[1,2,3,4] # f=1 and s=[2,3,4]
c1,c2,c3='hel' # c1='h',c2='e' and c3='l'
```

---

## 🔤 functions
1. function name follow snake-casing convention(Not mandatory to follow but best practice). def get_order_status()

2. followed by ''' quotes with docstring and then code we want to write.

3. Note - function should be declared first and then only can be called.

4. we can also provide default value to param to avoid error in case not passed. 

```python
def get_order_status(order_id=34):
    '''
    Docstring for get_order_status
    
    :param order_id: Description
    '''
    return f"order processed {order_id}!!!"

print(get_order_status(23)) #print: order processed 23!!!
print(get_order_status()) #print: order processed 34!!!
```

5. if we want to pass dynamic args to method, we can make use of '*' and '**' notation. for *args it will allow tuple to be passed as comma seprated values and for **kwargs dict to be passed as comma seprated key=value.
```python
def arg_test(*args): # it will take values as input
    print(type(args)) # print <class 'tuple'>
    print(args) 
    print(len(args))

arg_test(10,20,30) # print (10, 20, 30) and length as 3
arg_test((10,20,30)) # it will pass entire tuple as args[0] only. print ((10, 20, 30),) and length as 1
arg_test({"fruit":"apple","mango":23}) # it will pass entire dict as args[0] only. print ({'fruit': 'apple', 'mango': 23},) and length as 1

def kwarg_test(**kwargs): #it will take key,value pair as input
    print(type(kwargs)) # print <class 'dict'>
    print(kwargs) # print {'fruit': 'apple', 'mango': 23}
    for k,v in kwargs.items():
        print(f"key is : {k} and value is {v}")

kwarg_test(fruit="apple",mango=23)
#kwarg_test({"fruit":"apple","mango":23}) # give error as it will pass entire dict object as kwargs[0], but method expect key,value pair because of ** notation

def mixed(val,*tup,**dictionary): # order of normal arg, *args and **kwargs cannot be changed. they must be last with **kwargs at end
    '''
    * provide info that it is taking tuple, its not mandatory to be named args
    ** provide info it take dict, its not mandatory to be named kwargs
    '''
    print(type(val)) #<class 'int'>
    print(f"val is : {val}") #val is : 1
    print(type(tup)) #<class 'tuple'>
    print(f"tup is : {tup}")#tup is : (2, 3)
    print(type(dictionary))#<class 'dict'>
    print(f"dict is : {dictionary}")#dict is : {'k1': 'v1', 'k2': 'v2'}

mixed(1,2,3,k1="v1",k2="v2") # 1 will be pased as normal value, then remaining int as tuple and at last as dict
```
---

## 🔤 lambda
1. just like java we can write lambda to create anonymous function.

2. map and filter built-in method return iterators which can be used in for loop or can be converted to list.
```python
def square(num):
    return num**2

def is_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4]
res = map(square, nums)
print(list(res))
res = filter(is_even, nums)
print(list(res))
# lambda example
print(list(map(lambda x: x**2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
# square of even numbers
print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums))))
```

---

## 🔤 scope of variables
1. Local: they are local variables declared inside the function or lambda and not declared global in that function.
```python
myvar = 10
def sample_func():
    # local variable
    myvar=20

print(myvar) #print 10
sample_func()
print(myvar) #print 10
```
2. E: Enclosing function locals -- variables declared in the local scope of any and all enclosing functions (e.g. variable declared inside nested function)
```python
name= 'this is global string' #global

def greet():
    name='dummy' #enclosing local
    def hello():
        name='inside' #local
        print(f'Hello {name}') #print Hello inside
    hello()

greet()
```

3. G: Global -- variables declared at top level of module file or declared global in a def with in a file.
```python
# global example
def greet_global():
    global name 
    name ='new value'

greet_global()
print(name) # print new value
```

4. B: Built-in (Python) -- Names preassigned in the built-in names module: str, open, range, etc

5. in-case same variable name exists in multiple places preference is given in order: LEGB. i.e local given top priority

6. unlike java all the blocks like with,if/else,for/while,try/except does not create new scope. the variable declare here will take scope where block is created. example-
```python
def first():
    def second():
        x=20
    second()
    # print(x) #give error as x is not available outside second method

first()

for i in range(1,4):
    x=i
print(x) #print 3
```

---

## 🔤 oops
1. In python everything is an object. list, dict, str etc are built-in class. 
```python
print(type([1,2,3])) # print <class 'list'>
```

2. class: just like java we can create class with CamelCaseName. here __init__ work as constructor and self work as this keyword. it is not mandatory to use self just it should be first argument.
```python
class Sample(): #brackets are optional here
    pass

sample = Sample()
print(type(sample)) # print class '__main__.Sample'>

class Dog:
    is_mammal = True

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, status):
        print(f"woof! my name is {self.name} and i am {status}")


dog = Dog(breed="lab", name="bruno")
print(type(dog))  # print <class '__main__.Dog'>
print(type(dog.breed))  # print <class 'str'>
print(dog.breed)  # print lab
print(dog.name)  # print bruno
print(dog.is_mammal)  # print True
dog.bark("vaccinated")  # print woof! my name is bruno and i am vaccinated
```

3. class level variables are like static variable and all instances will share same value. and hence can be accessed via class name
```python
class Circle: #class Circle() will also work. brackets are optional
    pi = 3.14 # class level variable and remain same for all instances
    def __init__(self, radius=1):
        self.radius = radius
    def get_circumfrence(self):
        return 2*Circle.pi*self.radius #class level var can also be accessed via class name. they are like static 
    
my_circle1 = Circle()
print(my_circle1.get_circumfrence()) #print 6.28
my_circle2 = Circle(3)
print(my_circle2.get_circumfrence()) #print 18.84
print(Circle.pi) #print 3.14
```

4. Just like java we can also implement inheritance here. Example-
```python
class Animal:
    def __init__(self):
        print("Animal created")

    def eat(self):
        print("eating")

    def who_am_i(self):
        print("i am a animal")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self) # if we dont write this line, parent constructor not invoked
        #super().__init__() #both are same
        print("dog created")
    def who_am_i(self):
        print("i am a dog")
    def bark(self):
        print("woof!!!")

my_dog = Dog() #print Animal created. print Dog created
my_dog.who_am_i() #print i am a dog
my_dog.eat() #print eating
my_dog.bark() #print woof!!!
my_animal = Animal()#print Animal created
```

5. Python supports polymorphism dynamically (duck typing), not via static types.
```python
class Dog:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} woof")

class Cat:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} meow")

dog = Dog('pluto')  
cat = Cat('tom')
animals = [dog,cat]
for animal in animals: 
    animal.speak() ## Python only checks: does object have speak()?and hence it works.
```

6. Abstract class: extend class by ABC and provide abstractmethod
```python
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# animal_obj = Animal() #TypeError: Can't instantiate abstract class Animal with abstract method speak

class Dog(Animal):
    def speak(self): #in child class it is mandatory to override abstract method.
        print("woof!!")
dog = Dog() 
dog.speak()
```
7. If class does not extend ABC or does not provide any abstract method inside it. then object of the class can be created without any error.
```python
class Shape(ABC):
    def sides(self):
        pass

shape = Shape() #no error as ABC enforces abstraction only if @abstractmethod annotation method exists
shape.sides() #no error

class Hero:
    @abstractmethod
    def power(self):
        pass

hero = Hero() #no error as ABC parent does not exists
hero.power() #no error
```

8. Override built-in methods like len() str() 
```python

class Book:
    def __init__(self, title, collection):
        self.title = title
        self.collection = collection

mybook1 = Book('Harry Potter',[
    "Harry Potter and the Philosopher's Stone",
    "Harry Potter and the Chamber of Secrets",
    "Harry Potter and the Prisoner of Azkaban",
    "Harry Potter and the Goblet of Fire",
    "Harry Potter and the Order of the Phoenix",
    "Harry Potter and the Half-Blood Prince",
    "Harry Potter and the Deathly Hallows"
])

print(mybook1) #print <__main__.Book object at 0x7d9e3ca56cb0>
#print(f"collection has total books: {len(mybook1)}")  # give error as book does not have len() function

class BookSample:
    def __init__(self, title, collection):
        self.title = title
        self.collection = collection
    def __str__(self):
            return f"Title- {self.title}"

    def __len__(self):
            return len(self.collection)
    
mybook2 = BookSample('Shiva Trilogy',[
    "The Immortals of Meluha",
    "The Secret of the Nagas",
    "The Oath of the Vayuputras"
])

print(mybook2) #print Title-  Shiva Trilogy
print(f"collection has total books: {len(mybook2)}") #print collection has total books: 3
```

---

## 🔤 modules and packages
1. PyPI (Python Package Index) is a repository of open-source third-party Python packages. We use `pip` to install packages from PyPI.

2. Once a package is installed, we can import its modules, classes, or functions using the `import` statement.

3. A module is a `.py` file that contains Python code and can be imported into another Python file.

4. Packages are collection of modules. and should follow snakecase convention like method.example:

```python
mypackage/
├── __init__.py
├── first.py
└── second.py
first.py
def method_first():
   print("inside method_first of module first.py")
second.py
from first import method_first

method_first() # print inside method_first of module first.py
```

5. `__init__.py` is used to initialize a package. It is optional in Python 3.3+, but still commonly used for clarity and package-level configuration.

6. When you run a Python file directly, Python adds only the directory of that file to sys.path.(means current package and sub package only visible)
It does not automatically include the parent directory.
Because of this, if you run child.py directly and it tries to import parent.py from the parent folder, you may get a ModuleNotFoundError. in-order to avoid that run child file via module way like - python3 -m parent_folder.child_folder.child.

7. In production prefer design where main file present in root package invokes sub-package files. where each package provide specific behaviour.

### `__name__` and `'__main__'`

1. When a Python file is run **directly**, Python sets the special variable `__name__` to `"__main__"`. This allows us to execute code only when the file is run directly. 
When the same file is **imported as a module**, `__name__` is set to the module’s name.
```python
# one.py
if __name__ =='__main__':
  #initialization code, that will only executes when this file run directly.
else:
  #code it will get executed if someone import this file in some file.
```

2. Execution order-> When a module is imported, Python executes all top-level (root-level) code in that module once, from top to bottom. example- 
```python
from one import one_method
# 1. Executes all root-level code of one.py

def two_method():
    print("hello from two_method inside package_main_test package from two.py")

print("root level message from two.py")
# 2. Executed immediately

one_method()
# 3. Executes one_method

if __name__ == "__main__":
    print("main block of two.py")
    # 4. Executes only when two.py is run directly
else:
    print("main block else part of two.py")
    # 4. Executes only when two.py is imported

two_method()
# 5. Executes in both cases

```

---

## 🔤 Error and Exception handling
1. try, except and finally are block equivalent to try,catch and finally block of java. example-
```python
try:
    x=10
    y="20"
    print(x+y)
except TypeError:
    print("TypeError cannot add int with str")
except:
    print("For all other exception it will execute")
else:
    print("will execute if No exception")
finally:
    print("will execute always")
```

2. Just like while, except also has else, which get executed if no exception not caught. also like java try must have either except or finally. example of else use:
```python
flag = True
while flag:
    try:
        num = int(input("choose a number: "))
    except:
        print("provide number only!!")
    else:
        flag=False
else:
    print(f"Thanks for choosing {num}")
```


---

## 🔤 Pylint and unittest Library
1. Pylint is a static code analysis tool for Python. It checks code quality, coding standards (PEP 8), and possible errors. Pylint gives a score (0–10) for code quality.  
   Example: `pylint sample.py`

2. Common checks by pylint include unused variables and imports, naming convention issues, broad `except` usage, missing docstrings, and code complexity. All these impact the pylint score of a file.

3. The `unittest` library is a built-in Python module used to write unit test cases for Python functions.  
   Example to run a test file: `python3 -m tests.test_functions`

```python
import unittest
from functions import is_even

class TestFunctions(unittest.TestCase):

    def test_is_even_empty(self):
        my_list, message = is_even([])
        self.assertEqual(my_list, [])
        self.assertEqual(message, "success")

if __name__ == '__main__':
    unittest.main()
```

---

## 🔤 python decorators

1. unlike java python allow managing function inside a function.and any function can be treated just like normal object and hence can be assigned to variables, passed as arguments or return from function.this concept is used to create or use decorators in python.

2. a decorator is a function which takes another function as argument and will return a wrapped function with additional logic. It does not modify passed function behavior. example of log decorator function -
```python
def log(func):
    print("1. Inside log function") # 1
    def wrapper():
        print("4. Inside wrapper function before calling passed function") #4
        func()
        print("6. Inside wrapper function after calling passed function") #6
    print("2. exiting log function") # 2
    return wrapper

@log
def hello():
    print("5. inside hello function") #5

print("3. root level before calling hello") # 3
hello()
print("7. root level after calling hello") # 7
```

3. In the above example, the log decorator is executed when hello is defined, not when it is called.
calling hello() actually executes the wrapped function. below example cover what @log annotation do-
```python
def log(func):
    print("1. Inside log function") # 1
    def wrapper():
        print("4. Inside wrapper function before calling passed function") #4
        func()
        print("6. Inside wrapper function after calling passed function") #6
    print("2. exiting log function") # 2
    return wrapper

def hello():
    print("5. inside hello function") #5

decorated_hello = log(hello)

print("3. root level before calling returned function") # 3
decorated_hello()
print("7. root level after calling returned function") # 7
```
---

## 📦 Generators

1. When you want to process large data-set. it is not possible to store them in memory in list before processing. so, here generators are useful. A generator is a special type of iterator in Python.It generates values lazily (on demand when next method is called) instead of storing them in memory.

2. created using a function with yield keyword inside. example-
```python 
def create_cubes(n):
    return [i**3 for i in range(n)] #storing everything in memory as list first and then returning

for item in create_cubes(10):
    print(item)

def create_cube_via_generator(n):
    for i in range(n):
        yield i**3 # yield each number one by one.

for item in create_cube_via_generator(10): # internally invoke next method
    print(item)
```

3. Instead of using directly in for loop. we can iterate on each yield value one by one using next method. and once generator exhausted it will give StopIteration exception.
```python
def fibonaci(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b # swap values without extra variable

fib_generator = fibonaci(3)
print(fib_generator) # <generator object fibonaci at 0x707b5de42490>
print(next(fib_generator)) #print 1
print(next(fib_generator)) #print 1
print(next(fib_generator)) #print 2
#print(next(fib_generator)) #give exception - StopIteration
```

4. Limitations: unlike iterable objects like list- we cannot iterate by index, It only works in forward mode and once exhausted cannot be re-used.

| List              | Generator           |
| ----------------- | ------------------- |
| Stores all values | Generates on demand |
| High memory       | Low memory          |
| Faster access     | Slower access       |
| Indexable         | Not indexable       |

5. range method returns range object which is iterable and lazy.but it is not a generator.

6. Generators can be converted to a list if required using list(generator), but doing so defeats the memory advantage of generators.

7. Just like list comprehensions, we can create generators using generator comprehension with parentheses () instead of square brackets []-
```python
def create_cube_via_generator_comprehension(n):
    return (i**3 for i in range(n))    # return generator object 

for item in create_cube_via_generator_comprehension(10):
    print(item)
``` 

8. Strings are iterable, and calling iter() on a string returns an iterator object-
```python
s = 'hello'
obj = iter(s)
print(next(obj)) # 'h'
print(next(obj)) # 'e'
```

---

## 🔤 collections module

1. Counter: Used to count occurrences of items in an iterable and return the result in dictionary format.
```python
from collections import Counter
print(Counter([1,2,23,23,1,4,5,4,5,6]))  #Counter({1: 2, 23: 2, 4: 2, 5: 2, 2: 1, 6: 1})

c= Counter("aabbbcccccccaad")
print(c) #Counter({'c': 7, 'a': 4, 'b': 3, 'd': 1})
print(c.most_common(2)) # list of tuple as most common elements [('c', 7), ('a', 4)]
print(list(c)) #['a', 'b', 'c', 'd']
```

2. defaultdict: It allows setting a default value for a non-existent key. So if we try to access a key that does not exist, it will not raise a KeyError.
```python
from collections import defaultdict
defaultdict_obj = defaultdict(lambda: "Not Present") # default value for non existing key
defaultdict_obj['a'] = 1
print(defaultdict_obj['a']) #1
print(defaultdict_obj['b']) #Not Present
```

3. namedtuple: It allows assigning names to each index of a tuple. It resembles a lightweight class. they are immutable like tuple
```python
from collections import namedtuple
# namedtuple allows to create tuple with named fields.
Dog = namedtuple('Dog', ['age', 'breed', 'name']) 
dog1 = Dog(age=2, breed='Labrador', name='Tommy')
print(type(dog1))#<class '__main__.Dog'>
print(dog1) #Dog(age=2, breed='Labrador', name='Tommy')
print(dog1.age) #2
print(dog1.breed) #Labrador
print(dog1[2]) # Tommy
```

---

## 🔤 shutil and os module

1. os and shutil are built-in Python modules that provide useful methods for managing files and directories.

2. os.listdir(path) lists all files and folders in the given path. It does not list nested (subdirectory) contents.

3. os.walk(path) returns an iterator of tuples in the form (dirpath, dirnames, filenames). It traverses the entire directory hierarchy recursively.

```python 
import os
print(os.listdir('./packageA')) #['second.py', '__init__.py', 'packageB', 'app.py']
for dirpath, dirnames, filenames in os.walk('./packageA'):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)  

# output - 
# Current Path: ./packageA
# Directories: ['packageB']
# Files: ['second.py', '__init__.py', 'app.py']
# Current Path: ./packageA/packageB
# Directories: ['__pycache__']
# Files: ['first.py', '__init__.py']
# Current Path: ./packageA/packageB/__pycache__
# Directories: []
# Files: ['__init__.cpython-310.pyc', 'first.cpython-310.pyc']
```

4. os.unlink(path) deletes the file at the specified path.

5. os.rmdir(path) deletes a directory at the specified path. The directory must be empty.

6. shutil.rmtree(path) removes a directory and all its files and subdirectories recursively.

7. shutil.move(src, dest) moves a file or directory from the source path to the destination path.

---

## 🔤 datetime

datetime module has time, date and datetime class which provide different utility method to manage date time.

```python
t = datetime.time(4, 20, 1)

print(t)  # 04:20:01
print(f"hour: {t.hour}, minute: {t.minute}, second: {t.second}, microsecond: {t.microsecond}, tzinfo: {t.tzinfo}") # hour: 4, minute: 20, second: 1, microsecond: 0, tzinfo: None

d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05
print(f"Year: {d.year}, Month: {d.month}, Day: {d.day}") #Year: 2023, Month: 10, Day: 5

dt = datetime.datetime(2023, 10, 5, 4, 20, 1)  # combines date and time
print(dt)  # 2023-10-05 04:20:01
print(
    f"Year: {dt.year}, Month: {dt.month}, Day: {dt.day}, Hour: {dt.hour}, Minute: {dt.minute}, Second: {dt.second}"
) #Year: 2023, Month: 10, Day: 5, Hour: 4, Minute: 20, Second: 1
```

---

## 🔤 math and random module

1. The math module provides useful mathematical functions such as floor, ceil, and round, along with important constant values like e, inf, and nan.

```python
import math

print(math.floor(5.3)) #5
print(math.floor(5.9))#5
print(math.ceil(5.3))#6
print(math.ceil(5.9))#6
print(round(5.9))#6
print(round(5.2))#5
print(round(5.5))#6
print(round(4.5))#4, in case of .5 it always choose closest even number 

print(math.e)#2.718281828459045
print(math.inf)#inf
print(math.nan)#nan
```

2. random has randint to return random list. shuffle to shuffle list, choice to get random element from list, choices to get k element from list, sample to get k element from list without repetition.

| Function    | Description                                     |
| ----------- | ----------------------------------------------- |
| `choice()`  | Returns one random element                      |
| `sample()`  | Returns k elements **without repetition**       |
| `choices()` | Returns k elements **with possible repetition** |
| `shuffle()` | Randomly rearranges the list in-place           |

```python
import random

print(random.randint(0, 100))  # print new number every time
# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(
    101
)  # it set the sequence fix. so if same number is used it will generate same random number in order.
# You can run this as many times as you want, it will always return the same number
print(random.randint(0, 100))  # 74
print(random.randint(0, 100))  # 24
print(random.randint(0, 100))  # 69
my_list = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
random.shuffle(my_list) # suffle in-place
print(my_list)  # [9, 2, 3, 6, 1, 4, 10, 0, 8, 5]
print(random.choice(my_list))  # any random element from list
print(random.sample(my_list, 3))  # [6, 1, 3]
print(random.choices(my_list, k=3))  # [6, 1, 1]
```


---

## 🔤 regex

1. re.search() takes a pattern and a text string and returns the first matched object if a match is found, otherwise it returns None. 

2. The Match object returned by search() or match() provides useful methods like span, start, end method to provide index of matched string.

3. findall() method returns all matched text as a list of strings and if you want all matched object use finditer method

```python
import re

pattern = r"p\w{4}"
match = re.search(pattern,"my phone is a super phone")
#search matches the first instance only. not all.
print(match) #<re.Match object; span=(3, 8), match='phone'>
print(match.span()) #(3, 8)
print(match.start()) #3
print(match.end()) #8
print(match.string) #my phone is a super phone
print(match.group()) #return actual matched text - phone

#To find all matches use findall method
match_all = re.findall(pattern,"my phone is a super phone")
print(match_all) # print phone phone

# to get entire match object instead of just matched string use finditer
for match in re.finditer(pattern,"my phone is a super phone"):
    print(match.group()) # print phone twice
```

4. Common regex character classes:

| Character | Description       | Example Pattern Code | Example Match |
|-----------|------------------|----------------------|---------------|
| \d        | A digit          | file_\d\d            | file_25       |
| \w        | Alphanumeric     | \w-\w\w\w            | A-b_1         |
| \s        | White space      | a\sb\sc              | a b c         |
| \D        | A non digit      | \D\D\D               | ABC           |
| \W        | Non-alphanumeric | \W\W\W\W\W           | *-+=)         |
| \S        | Non-whitespace   | \S\S\S\S             | Yoyo          |

5. quantifiers: 

| Character | Description               | Example Pattern Code | Example Match  |
| --------- | ------------------------- | -------------------- | -------------- |
| +         | Occurs one or more times  | Version \w-\w+       | Version A-b1_1 |
| {3}       | Occurs exactly 3 times    | \D{3}                | abc            |
| {2,4}     | Occurs 2 to 4 times       | \d{2,4}              | 123            |
| {3,}      | Occurs 3 or more          | \w{3,}               | anycharacters  |
| *         | Occurs zero or more times | A*B*C*               | AAACC          |
| ?         | Once or none              | plurals?             | plural         |
