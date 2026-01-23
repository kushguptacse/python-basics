#global
myvar = 10
def sample_func():
    # local variable
    myvar=20

print(myvar) #print 10
sample_func()
print(myvar) #print 10

# enclosing function example
name= 'this is global string' #global

def greet():
    name='dummy' #enclosing local
    def hello():
        name='inside' #local
        print(f'Hello {name}') #print Hello inside
    hello()

greet()
# global example
def greet_global():
    global name_check 
    name_check ='new value'

greet_global()
print(name_check) # print new value

def first():
    def second():
        x=20
    second()
    # print(x) #give error as x is not available outside second method

first()

with open('myfile.txt') as sample:
    content = sample.read()
    y=100
print(y) # print 100

for i in range(1,4):
    x=i
print(x) #print 3