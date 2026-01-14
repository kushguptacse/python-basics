myset= set()
myset.add('hello') # in set element are added using add method. only list has append not set and only set has add not list.
print(myset) # print {'hello'}
myset = set("hello") 
print(myset) # print {'h', 'e', 'l', 'o'}
myset = set([1,2,3,4])
print(myset) # print {1,2,3,4}
myset = set((1,2,3))
print(myset)# print {1,2,3}
myset = {1,2,3}
print(myset)# print {1,2,3}
myset = {1,2,3,2}
print(myset)# print {1,2,3}
myset = {} # valid, but it will create empty dict not set.

