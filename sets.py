myset = set()
myset.add(
    "hello"
)  # in set element are added using add method. only list has append not set and only set has add not list.
print(myset)  # print {'hello'}
myset = set("hello")
print(myset)  # print {'h', 'e', 'l', 'o'}
myset = set([1, 2, 3, 4])
print(myset)  # print {1,2,3,4}
myset = set((1, 2, 3))
print(myset)  # print {1,2,3}
myset = {1, 2, 3}
print(myset)  # print {1,2,3}
myset = {1, 2, 3, 2}
print(myset)  # print {1,2,3}
myset = {}  # valid, but it will create empty dict not set.

test_set = {1, 2, 4, 5}
test_set.clear()  # None
print(test_set)  # empty set set()
test_set = {1, 2, 4, 5}
print(test_set.copy())  # return shallow copy of set
print("$$$$$$$$$$$$")
set1 = {1, 2, 3}
set2 = {2, 4, 6}
print(set1.difference(set2))  # {1, 3}
set1.discard(3) 
print(set1) # {1,2}
set1.difference_update(set2) # return set1 after removing set2
print(set1) # {1}

set1 = {1,2,3}
set2 = {1,3,4,2}
print(set1.issubset(set2)) # True