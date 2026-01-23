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