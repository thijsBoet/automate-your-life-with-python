from pathlib import Path

folder = Path('2022-csv-renamed')
search_text = '2022-01-01'

for path in folder.glob('**/*.csv'):
    if search_text in path.name:
        print(path)
        print(path.absolute())
