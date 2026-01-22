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
    global name 
    name ='new value'

greet_global()
print(name) # print new value
