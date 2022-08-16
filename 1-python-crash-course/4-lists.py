countries = ['Canada', 'USA', 'Mexico', 'France', 'Germany', 'Italy', 'Spain']
# insert at last index
countries.append('China')
# insert at certain index
countries.insert(1, 'Brazil')
print(countries[-1])
# countries[start: stop]
print(countries[2:5])
# remove Mexico from the list
countries.remove('Mexico') # del countries[2] also works
# remove last item from the list
countries.pop()
cities = ['Toronto', 'Vancouver', 'Paris', 'Berlin', 'Rome', 'Madrid']
countries_and_capitals = countries.extend(cities)  # countries + cities also valid
# nested list
nested_list = [cities, countries]

numbers = [5,10,7,2,1,9,12,8,15,6]
sorted_numbers = numbers.sort()
reversed_sorted_numbers = numbers.sort(reverse=True)
updated_first_number = numbers[0] = 1000
# [:] includes all items in the list
copy_list = countries[:]
copy_list2 = countries.copy()
