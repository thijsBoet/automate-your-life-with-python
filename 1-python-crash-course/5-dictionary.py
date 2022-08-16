my_dict = {
	'key1': 'value1',
	'key2': 'value2',
	'key3': 'value3'
}

my_data = {
	'name': 'Matthijs Boet',
	'age': 40,
	'city': 'Rotterdam'
}
# print keys
print(my_data.keys())
# print values
print(my_data.values())
# print key and value
print(my_data.items())

# add new key and value
my_data['height'] = '1.94 meters'
# update value
my_data.update({'age': 41})

# copy dictionary as reference type
dictionary_copy = my_data.copy()
# copy dictionary where values are linked to new values
dictionary_copy2 = my_data

# remove item by key
my_data.pop('height')
# alternative way to remove item by key
del my_data['age']
# remove dictionary
my_data.clear()
# remove dictionary
del my_data