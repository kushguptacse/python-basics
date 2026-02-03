def create_cubes(n):
    return [i**3 for i in range(n)] #storing everything in memory as list and then returning


for item in create_cubes(10):
    print(item)

def create_cube_via_generator(n):
    for i in range(n):
        yield i**3 # yield each number one by one.

print(create_cube_via_generator(1)) # <generator object create_cube_via_generator at 0x707b5de42490>

for item in create_cube_via_generator(10):
    print(item)

def create_cube_via_generator_comprehension(n):
    return (i**3 for i in range(n))  # return generator object

print("******")
for item in create_cube_via_generator_comprehension(10): # iterate over generator.
    print(item)

def fibonaci(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b # swap values without extra variable

print(fibonaci(1)) # <generator object fibonaci at 0x707b5de42490>

for item in fibonaci(10):
    print(item)


fib_generator = fibonaci(3)

print(next(fib_generator)) #print 1
print(next(fib_generator)) #print 1
print(next(fib_generator)) #print 2
#print(next(fib_generator)) #give exception - StopIteration


# convert string into iterator
s = 'hello'
obj = iter(s)
print(next(obj)) # 'h'
print(next(obj)) # 'e'