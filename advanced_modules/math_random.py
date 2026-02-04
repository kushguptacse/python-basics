import math

print(math.floor(5.3))  # 5
print(math.floor(5.9))  # 5
print(math.ceil(5.3))  # 6
print(math.ceil(5.9))  # 6
print(round(5.9))  # 6
print(round(5.2))  # 5
print(round(5.5))  # 6
print(round(4.5))  # 4, in case of .5 it always choose closest even number

print(math.e)  # 2.718281828459045
print(math.inf)  # inf
print(math.nan)  # nan

print("***********************************************")

import random

print(random.randint(0, 100))  # print new number every time
# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(
    101
)  # it set the sequence fix. so if same number is used it will generate same random number in order.
# You can run this as many times as you want, it will always return the same number
print(random.randint(0, 100))  # 74
print(random.randint(0, 100))  # 24
print(random.randint(0, 100))  # 69

my_list = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]

random.shuffle(my_list)
print(my_list)  # [9, 2, 3, 6, 1, 4, 10, 0, 8, 5]

print(random.choice(my_list))  # any random element from list
print(random.sample(my_list, 3))  # [6, 1, 3]
print(random.choices(my_list, k=3))  # [6, 1, 1]
