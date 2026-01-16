def get_order_status(order_id=34):
    """
    Docstring for get_order_status

    :param order_id: Description
    """
    return f"order processed {order_id}!!!"


print(get_order_status(23))  # print: order processed 23!!!
print(get_order_status())  # print: order processed 34!!!

def is_even(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens,"success"

my_list, message = is_even([10,21,30])
print(f"{message}: {my_list}")

my_list, message,third = is_even([10,21,30]) #error as third value not returned and hence cannot be unpacked.