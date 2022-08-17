from pathlib import Path

folder = Path('txt_files')
# txt_paths = folder.glob('**/*.txt')
# csv_paths = folder.glob('**/*.csv')

# def text_to_csv(paths):
# 	for path in enumerate(paths):
# 		new_path_name = path.with_name(f'{path.stem}.csv')
# 		path.rename(new_path_name)

# def csv_to_text(paths):
# 	for path in enumerate(paths):
# 		new_path_name = path.with_name(f'{path.stem}.txt')
# 		path.rename(new_path_name)


# text_to_csv(txt_paths)
# csv_to_text(csv_paths)

for path in list(folder.iterdir()):
    if(path.suffix == '.txt'):
        new_extension = path.with_suffix('.csv')
        path.rename(new_extension)

for path in folder.glob('**/*.csv'):
    print(path) 
    new_extension = path.with_suffix('.txt')
    path.rename(new_extension)
