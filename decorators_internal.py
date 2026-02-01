def log(func):
    print("1. Inside log function") # 1
    def wrapper():
        print("4. Inside wrapper function before calling passed function") #4
        func()
        print("6. Inside wrapper function after calling passed function") #6
    print("2. exiting log function") # 2
    return wrapper

def hello():
    print("5. inside hello function") #5

decorated_hello = log(hello)

print("3. root level before calling returned func") # 3
decorated_hello()
print("7. root level after calling returned func") # 7
