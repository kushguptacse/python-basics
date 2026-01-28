from one import one_method # first: it print all root level messages  and else block of __name__ check in top to bottom order

def two_method():
    print("hello from two_method inside package_main_test package from two.py")

print("root level message from two.py") # second: print root level message from two.py
one_method() # third: print one_method statements

if __name__ == "__main__": 
    print("main block of two.py") # fourth:  print if run directly
else:
    print("main block else part of two.py") # fourth: wont print if run directly, only in case of import it is executed.

two_method() # fifth: print hello from two_method inside package_main_test package from two.py
