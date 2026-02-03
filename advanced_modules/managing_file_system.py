import os
list_dir = os.listdir('./packageA')
print(list_dir) #['second.py', '__init__.py', 'packageB', 'app.py']

print("-------------------")
for dirpath, dirnames, filenames in os.walk('./packageA'):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)  

# output - 
# Current Path: ./packageA
# Directories: ['packageB']
# Files: ['second.py', '__init__.py', 'app.py']
# Current Path: ./packageA/packageB
# Directories: ['__pycache__']
# Files: ['first.py', '__init__.py']
# Current Path: ./packageA/packageB/__pycache__
# Directories: []
# Files: ['__init__.cpython-310.pyc', 'first.cpython-310.pyc']