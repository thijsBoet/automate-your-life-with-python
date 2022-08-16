import os
from pathlib import Path

path_os = os.getcwd()
path_Path = Path.cwd()

# string
print(type(path_os), path_os)
# path object
print(type(path_Path), path_Path)
# get last element of path
print(path_Path.name)
# give variable a path to a certain file
path = Path('text/expenses.txt')
# print parts of path in tuple
print(path.parts)
# print file name
print(path.name)
# print file name without extension
print(path.stem)
# print file extension
print(path.suffix)
