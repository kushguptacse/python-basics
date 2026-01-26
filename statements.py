name = "kush"
if name == "kush":
    print(f"name is {name}")
elif name == "pizza":
    print(f"name is {name}")
else:
    print(f"name is {name}")

for item in [1, 2, 3]:
    if item % 2 == 0:
        print(f"item is even : {item}")

# iterate over string
for letter in "hello world":
    print(letter)

# iterate over tuple
for tup in (1, 2, 3):
    print(tup)

# iterate over list of tuple
for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(f"first tuple {a} and second tuple {b}")

# iterate over dictionary using keys
sample_dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
for key in sample_dict:
    print(f"elements with key {key} is {sample_dict[key]}")

# iterate over dictionary using dictionary entry
for key, item in sample_dict.items():  # tuple
    print(f"elements with key {key} is {item}")

# while loop

x = 0
while x < 5:
    print(f"x is {x}")
    x += 1
else:
    print(f"x is {x} now") #x is 5 now

# pass, continue, break
for it in [1, 2, 3]:
    pass  # now this code wont execute, it is just to avoid python to give error of writng empty loop.

for it in [1, 2, 3]:
    if it % 2 == 0:
        continue
    print(it)

for it in [1, 2, 3]:
    if it % 2 == 0:
        break
    print(it)
print("000000000000000000000000000000000000000000000000000000")
coord=(2,5)
x,y=coord #x=2,y=5
print(f"x {x} and y {y}")
a,b={1,2} # a=1,b=2
print(f"x {a} and y {b}")
f,*s=[1,2,3,4] # f=1 and s=[2,3,4]
print(f"x {f} and y {s}")
c1,c2,c3='hel' # c1='h',c2='e' and c3='l'
print(f"x {c1} and y {c2}")
l1,l2 = [1,2,3] # it will give error as three variables required'