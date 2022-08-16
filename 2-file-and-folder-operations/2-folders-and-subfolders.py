from pathlib import Path
import calendar

# create a new folder (overwrites if exists with exist_ok=True flag)
Path('new_folder').mkdir(exist_ok=True)
# create multiple sub-folders
Path('new_folder/subfolder1/subfolder2').mkdir(parents=True, exist_ok=True)

# create list with all the month names
month_names = list(calendar.month_name[1:])
days = ['Day 1', 'Day 10', 'Day 20', 'Day 30']

# create a new folder a month at a time
Path('2022/January').mkdir(parents=True, exist_ok=True)

# create a folder for each month in the year
for index, month in enumerate(month_names):
		for day in days:
			Path(f'2022/{index + 1}. {month}/{day}').mkdir(parents=True, exist_ok=True)