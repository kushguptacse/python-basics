my_list = [100,"hello",23.45,True]
print(f"my_list: {my_list}") # print my_list: [100, 'hello', 23.45, True]
print(f"my_list[0]: {my_list[0]}") # print my_list[0]: 100
print(f"my_list[1]: {my_list[1]}") # print my_list[1]: hello
print(f"my_list[1][0]: {my_list[1][0]}") # print my_list[1][0]: h
print(f"my_list[1:]: {my_list[1:]}") # print my_list[1:]: ['hello', 23.45, True]
print(f"my_list[1:3]: {my_list[1:3]}") # print my_list[1:3]: ['hello', 23.45]
print(f"my_list[::-1]: {my_list[::-1]}") # print my_list[::-1]: [True, 23.45, 'hello', 100]
print(f"length of my_list: {len(my_list)}") # print length of my_list: 4
another_list = [200, "world"] 
combined_list = my_list + another_list
print(f"combined_list: {combined_list}") # print combined_list: [100, 'hello', 23.45, True, 200, 'world']
my_list[0] = 500
print(f"modified my_list: {my_list}") # print modified my_list: [500, 'hello', 23.45, True]
my_list.append("new item")
print(f"my_list after append: {my_list}") # print my_list after append: [500, 'hello', 23.45, True, 'new item']
print(f"item popped from my_list: {my_list.pop()}") # print item popped from my_list: new item
print(f"my_list after pop: {my_list}") # print my_list after pop: [500, 'hello', 23.45, True]
print(f"item popped from my_list at index 1: {my_list.pop(1)}") # print item popped from my_list at index 1: hello
print(f"my_list after pop at index 1: {my_list}") # print my_list after pop at index 1: [500, 23.45, True]
my_list.remove(500)
print(f"my_list after remove: {my_list}") # print my_list after remove: [23.45, True]
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort()
print(f"sorted num_list: {num_list}") # print sorted num_list: [1, 2, 5, 5, 6, 9]
num_list.reverse()
print(f"reversed num_list: {num_list}") # print reversed num_list: [9, 6, 5, 5, 2, 1]