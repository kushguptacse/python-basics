class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} woof")


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} meow")


dog = Dog("pluto")
cat = Cat("tom")
animals = [dog, cat]
for animal in animals:
    animal.speak()


class Book:
    def __init__(self, title, collection):
        self.title = title
        self.collection = collection

mybook1 = Book('Harry Potter',[
    "Harry Potter and the Philosopher's Stone",
    "Harry Potter and the Chamber of Secrets",
    "Harry Potter and the Prisoner of Azkaban",
    "Harry Potter and the Goblet of Fire",
    "Harry Potter and the Order of the Phoenix",
    "Harry Potter and the Half-Blood Prince",
    "Harry Potter and the Deathly Hallows"
])

print(mybook1) #print <__main__.Book object at 0x7d9e3ca56cb0>
#print(f"collection has total books: {len(mybook1)}")  # give error as book does not have len() function.


class BookSample:
    def __init__(self, title, collection):
        self.title = title
        self.collection = collection
    def __str__(self):
            return f"Title- {self.title}"

    def __len__(self):
            return len(self.collection)
    

mybook2 = BookSample('Shiva Trilogy',[
    "The Immortals of Meluha",
    "The Secret of the Nagas",
    "The Oath of the Vayuputras"
])

print(mybook2) #print Title-  Shiva Trilogy
print(f"collection has total books: {len(mybook2)}") #print collection has total books: 3