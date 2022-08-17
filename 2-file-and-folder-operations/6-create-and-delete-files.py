from pathlib import Path
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    # create file
    with open(f'test{i}.txt', 'w') as file:
        # write file
        file.write('Testing this')

for path in Path('./').glob('test[1-8].txt'):
    # delete files
    path.unlink()