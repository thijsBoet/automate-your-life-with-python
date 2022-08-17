from pathlib import Path

# create a folder and file
Path('test').mkdir(exist_ok=False)
my_file = Path('test/expenses.txt')
my_file.touch(exist_ok=False)

# rename a folder
path = Path('test')
path.rename('new_test')

# rename a file within a folder
path = Path('new_test/expenses.txt')
new_path_name = path.with_name('expenses.txt')
print(new_path_name)
path.rename('new_test/expenses-januari.txt')

# get path of immediate subdirectories
folder = Path('2022')
for path in list(folder.iterdir()):
	print(path)

# get path of all subdirectories
paths = folder.glob('**/*')

for path in paths:
  print(path)

# get path of all files
for path in paths:
  if path.is_file():
    print(path)

# get path of all subdirectories the only have .py files
folder = Path('.')

for path in folder.glob('**/*.py'):
  print(path)