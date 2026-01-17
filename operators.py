print("operator examples")
# useful operators
for num in range(0, 11):
    print(num)

for num in range(0, 11, 2):  # step size 2
    print(num)

word = "abcde"
i = 0
for item in word:
    print(f"item at index {i} is {word[i]}")
    i += 1

for i, val in enumerate(word): # enumerate converts iterable into tuple with index and value
    print(f"item at index {i} is {val}")

nums = [1,2,35]
for i, val in enumerate(nums):
    print(f"item at index {i} is {val}")

print("zip example")
l1 = [1,2,3]
l2 = ['a','b','c']
l3 = [1.1,2.2,3.3]

for x,y,z in zip(l1,l2,l3):
    print(f"{x},{y},{z}")

l4=[False]
for x,y in zip(l1,l4):
    print(f"{x},{y}")

print("in operator")

if 1 in [1,2,3]:
    print("exists")

d={'k1':'v1',"k2":"v2"}
if "k1" in d:
    print("exists")

if "v1" in d.values():
    print("exists")

print(f"min elment in list is : {min(l1)}")
print(f"max elment in list is : {max(l1)}")

from random import shuffle, randint
l = [1,2,3,4]
shuffle(l)
print(l)
var = randint(0,100)
print(var)

first = input('enter a number here:')
print(int(first)) # input is read as str value