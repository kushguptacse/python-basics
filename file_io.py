myfile = open('myfile.txt') # of complete path can be given
content = myfile.read() 
print(content) # prints file entire content
content = myfile.read()
print(content) # prints nothing as file pointer is at the end of file
myfile.seek(0) # move file pointer to start of the file
content = myfile.read()
print(content) # prints file entire content again
myfile.seek(0)
lines = myfile.readlines()
print(lines) # prints ['hello this is txt file\n', 'first line\n', 'second line']
myfile.close() # if not closed it may lead to memory leak

with open('myfile.txt') as myfile2: # automatically closes the file after with block is executed
    content2 = myfile2.read()
print(content2) # prints file entire content

with open('myfile.txt','r') as myfile2: # open file in read mode and is default mode
    content2 = myfile2.read()
    # myfile2.write('new line') # will give error as file is opened in read mode
print(content2) # prints file entire content

with open('myfile.txt','w') as myfile2: # open file in write mode and overwrites existing content
    myfile2.write('new line')
    # myfile2.read() # will give error as file is opened in write mode

with open('myfile.txt','r') as myfile3:
    content3 = myfile3.read()
    print(content3) # prints new line

with open('myfile1.txt','a') as myfile4: # open file in append mode and creates file if not exists
    myfile4.write('\nappended line')