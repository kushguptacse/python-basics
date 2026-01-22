mylist = [1, 2, 3]
print(type(mylist))  # print <class 'list'>

myset = {1, 2}
print(type(myset))  # print <class 'set'>


class Sample:
    pass


sample = Sample()
print(type(sample))  # print class '__main__.Sample'>


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


class Circle: #class Circle() will also work. brackets are optional
    pi = 3.14  # class level variable and remain same for all instances

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumfrence(self):
        return (
            2 * Circle.pi * self.radius
        )  # class level var can also be accessed via class name. they are like static


my_circle1 = Circle()
print(my_circle1.get_circumfrence())  # print 6.28
my_circle2 = Circle(3)
print(my_circle2.get_circumfrence())  # print 18.84
print(Circle.pi)  # print 3.14
