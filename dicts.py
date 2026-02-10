sample = {"name": "kush", "age": 34, "k2": [1, 2, 3], "k3": {"nested": 900}}
print(sample["name"])  # print kush
print(sample["k2"][1])  # print 2
print(sample["k3"]["nested"])  # print 900
print(sample.keys())  # print dict_keys(['name', 'age', 'k2', 'k3'])
print(sample.values())  # print dict_values(['kush', 34, [1, 2, 3], {'nested': 900}])
print(
    sample.items()
)  # print dict_items([('name', 'kush'), ('age', 34), ('k2', [1, 2, 3]), ('k3', {'nested': 900})])
sample["name"] = "agent"
print(sample["name"])  # print agent
data = {1: "int key", "1": "string key"}
print(data[1])  # int key
print(data["1"])  # string key
sample[2351] = "kk"
print(
    sample
)  # print {'name': 'agent', 'age': 34, 'k2': [1, 2, 3], 'k3': {'nested': 900}, 2351: 'kk'}

print("*******************Advanced dictionary*********************")
dict_num = {x: x**2 for x in range(4)}
print(dict_num)  # {0: 0, 1: 1, 2: 4, 3: 9}

names = ["a", "b"]
age = [23, 34]
dict1 = {names[x]: age[x] for x in range(len(names))}  # dict comprehension
for k, v in dict1.items():
    print(f"key: {k}, value: {v}")

for k in dict1.keys():
    print(f"key: {k}") # print keys

for k in dict1:
    print(f"key: {k}") # print keys

for v in dict1.values():
    print(f"value: {v}") # print values
