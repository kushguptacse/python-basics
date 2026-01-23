def arg_test(*args): # it will take values as input
    print("*********")
    print(type(args)) # print <class 'tuple'>
    print(args) 
    print(len(args))

arg_test(10,20,30) # print (10, 20, 30) and length as 3
arg_test((10,20,30)) # it will pass entire tuple as args[0] only. print ((10, 20, 30),) and length as 1
arg_test({"fruit":"apple","mango":23}) # it will pass entire tuple as args[0] only. print ({'fruit': 'apple', 'mango': 23},) and length as 1

def kwarg_test(**kwargs): #it will take key,value pair as input
    print("################")
    print(type(kwargs)) # print <class 'dict'>
    print(kwargs) # print {'fruit': 'apple', 'mango': 23}
    for k,v in kwargs.items():
        print(f"key is : {k} and value is : {v}")

kwarg_test(fruit="apple",mango=23)
#kwarg_test({"fruit":"apple","mango":23}) # give error as it will pass entire dict as kwargs[0], but method expect key,value pair

def mixed(val,*tup,**dictionary): # order of normal arg, *args and **kwargs cannot be changed. they must be last with **kwargs at end
    '''
    * provide info that it is taking tuple, its not mandatory to be named args
    ** provide info it take dict, its not mandatory to be named kwargs
    '''
    print("--------------------")
    print(type(val)) #<class 'int'>
    print(f"val is : {val}") #val is : 1
    print(type(tup)) #<class 'tuple'>
    print(f"tup is : {tup}")#tup is : (2, 3)
    print(type(dictionary))#<class 'dict'>
    print(f"dict is : {dictionary}")#dict is : {'k1': 'v1', 'k2': 'v2'}

mixed(1,2,3,k1="v1",k2="v2") # 1 will be pased as normal val, then remaining as tuple and at last dict