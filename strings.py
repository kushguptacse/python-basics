val = "hello world"
print(f"val: {val}")
print(f"val: {val[0]}")
print(f"slicing ..............")
print(f"val[7:11]: {val[7:11]}")
print(f"val[-1]: {val[-1]}")
print(f"val[7:11:2]: {val[7:11:2]}")
print(f"reverse of val: {val[::-1]}")
print(f"length of val: {len(val)}")
print(f"val[1::-1]: {val[1::-1]}")

x = "10"
x=x+'20'
print(x)

print('the {2} {1} {0}'.format('fox','brown','quick') )
x = 'the {2} {1} {0}'.format('fox','brown','quick')  # the quick brown fox 
print(x)
x = 'the {q} {b} {f}'.format(q='quick',b='brown',f='fox') # the quick brown fox
print(x)
x = 'the {f} {f} {f}'.format(q='quick',b='brown',f='fox') # the fox fox fox
print(x)
x = 'the {1} {1} {1}'.format('quick','brown','fox') # the brown brown brown
print(x)

print('float formatting .............. ')
result = 100/777
print(f"result: {result}") # print result: 0.1287001287001287
print(f"result: {result:.3f}") # print result: 0.129
print(f"result: {result:10.5f}") # print result:    0.12870

# Example using String interpolation using f"" syntax introduced in python 3.6
name = "John"
age = 30
print(f"name: {name} and age: {age}.") # print name: John and age: 30.
print(f"name: {name.upper()} and age: {age + 5} and marks: {result:.3f}.") # print name: JOHN and age: 35 and marks: 0.129.
print("----------------join example----------------")
print(" ".join("hello world"))  # print h e l l o   w o r l d
print(" ".join(["hello","world","guys"]))  # print hello world guys
print(f"capitalize method result of helloworld is : {'helloworld'.capitalize()}") # print Helloworld
