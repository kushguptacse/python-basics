from collections import Counter
#Used to count occurrences of items in an iterable and return the result in dictionary format.
print(Counter([1,2,23,23,1,4,5,4,5,6]))  #Counter({1: 2, 23: 2, 4: 2, 5: 2, 2: 1, 6: 1})

c= Counter("aabbbcccccccaad")
print(c) #Counter({'c': 7, 'a': 4, 'b': 3, 'd': 1})
print(c.most_common(2)) # list of tuple as most common elements [('c', 7), ('a', 4)]
print(list(c)) #['a', 'b', 'c', 'd']

from collections import defaultdict

# It allows to set default value for non existing key. so if we try to access non existing key, it will not give KeyError
defaultdict_obj = defaultdict(lambda: "Not Present") # default value for non existing key
defaultdict_obj['a'] = 1
print(defaultdict_obj['a']) #1
print(defaultdict_obj['b']) #Not Present

defaultdict_obj = defaultdict(int) # default value 0 for non existing key
defaultdict_obj['a'] = 1
print(defaultdict_obj['a']) #1
print(defaultdict_obj['b']) #0

from collections import namedtuple
# namedtuple allows to create tuple with named fields.
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
dog1 = Dog(age=2, breed='Labrador', name='Tommy')
print(type(dog1))#<class '__main__.Dog'>
print(dog1) #Dog(age=2, breed='Labrador', name='Tommy')
print(dog1.age) #2
print(dog1.breed) #Labrador
print(dog1.name) #Tommy 
print(dog1[2]) # Tommy