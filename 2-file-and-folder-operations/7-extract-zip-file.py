from pathlib import Path
import zipfile

current_dir = Path('.')
target_dir = Path('temp')

for path in current_dir.glob('*.zip'):
    with zipfile.ZipFile(path, 'r') as zip_obj:
        zip_obj.extractall(path=target_dir)