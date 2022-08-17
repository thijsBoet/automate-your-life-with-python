from pathlib import Path
import re

# folder = Path('2022')
# paths = folder.glob('**/*.csv')
# for index, path in enumerate(paths):
#     new_path_name = path.with_name(f'expense{path.parts[0]}{path.parts[1]}{path.parts[2]}.csv')
#     path.rename(new_path_name)
#     print(new_path_name)

folder = Path('2022')
paths = folder.glob('**/*.csv')
for index, path in enumerate(paths):
    print(path.parts)
    day = path.parts[-2]
    day_number = int(re.findall('\d+', day)[0])
    month = path.parts[-3]
    month_number = int(re.findall('(\d+).', month)[0])
    year = path.parts[0]

    new_path_name = path.with_name(f'expense-{year}-{month_number:02d}-{day_number:02d}.csv')
    path.rename(new_path_name)