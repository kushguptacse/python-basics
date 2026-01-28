# nesting exception example

try:
    x=20
    print(x+"20")
except TypeError:
    print("if type error occurred it will execute")
except:
    print("all exceptions")
else:
    print("will execute if No exception")
finally:
    print("always executed")

print("-------------------")
flag = True
while flag:
    try:
        num = int(input("choose a number: "))
    except:
        print("provide number only!!")
    else:
        flag=False
else:
    print(f"Thanks for choosing {num}")

