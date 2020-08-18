# A Dictionary is a collection that is unordered, chanagableand indexed. No duplicate member is allowed for this

#create a Dictionary

person_detail = {
    'first_name': 'fortunes',
    'last_name': 'onyekwere',
    'age': 21
}

# Use of a constructor

person_details2 = dict(first_name = 'fortunes', last_name='onyekwere')

print(person_detail)

# Getting a value
print(person_detail['first_name'])

# Add key value
person_detail['phone_number'] = '+2347067162698'
print(person_detail)

# Get dictionary keys
print(person_detail.keys())

# Get dictionary items
print(person_detail.items())

#copy dictionary
person_information = person_detail.copy()
print(person_information)

# Remove item
del  (person_detail['last_name'])
person_detail.pop('phone_number')
print(person_detail)

# Clear
#person_detail.clear()
print(person_detail)

# Get length
print(len(person_detail))

# make a list of dictionaries
persons = [
    {'name':'fortunes','age': 21, 'phone_number': '+234706012548'},
    {'name':'fortunes','age': 21, 'phone_number': '+2347083915552'},
    {'name':'ola','age': 30, 'phone_number': '+2348156243419'},
]

print(persons[1]['name'])
print(persons[0]['age'])
print(persons[2]['phone_number'])
print(persons[2]['age'])