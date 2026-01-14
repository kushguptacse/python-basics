val  = True
print(val)
val = False
print(val)
print(type(val)) # print <class 'bool'>
val = None
print(val) # print None
print(type(val)) # print <class 'NoneType'>

print(f"'2'==2: {'2'==2}") # print False
print(f"2==2.0: {2==2.0}") # print True as for float python just check value.
print(f"2!=3: {2!=3}") # print True
print(f"2!=2.0: {2!=2.0}") # print False
print(f"1<2<3: {1<2<3}")# print True. it is evaluated left to right
print(f"1<2>3: {1<2>3}")# print False. it is evaluated left to right

print(f"1<2 and 2<3: {1<2 and 2<3}")# print True.
print(f"1<2 or 2<3: {1<2 or 2>3}")# print True.
print(f"not 1==1: {not 1==1}")# print False.
print(f"1!=1: {1!=1}")# print False.
