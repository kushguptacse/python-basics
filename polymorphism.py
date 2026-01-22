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
    animal.speak()