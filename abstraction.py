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
