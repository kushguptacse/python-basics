def square(num):
    return num**2


def is_even(num):
    return num % 2 == 0


nums = [1, 2, 3, 4]
# map and filter method generate output as generator which can be used in for loop or can be converted to list.
res_generator = map(square, nums)
print(list(res_generator))


res_generator = filter(is_even, nums)
print(list(res_generator))

# lambda example
print(list(map(lambda x: x**2, nums)))#[1, 4, 9, 16]
print(list(filter(lambda x: x % 2 == 0, nums)))#[2, 4]
# square of even numbers
print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums))))#[4, 16]
