'''
# Strings in python are surrouneded by either single or double 
quotation marks. let's look at string formatting and some string 
methods

name = 'Brad'
age = 37

# Concatenate 
print ('hello, my name is ' + ' and i am ' + str (age))

# String formatting 

# Arguments b t position
print ('My name is {name} and i am {age}'. format (name=name, age=age))

# F-Strings (3.6+)
print (f'Hello, my name is {name} and i am  {age}')

# String Methods

s = 'helloworld'

# Capitalize string
print (s.capitalize())

# Make all uppercase
print (s.upper())

# Make all lowercase
print (s.lower())

# Swap case
print (s. swapcase())

# Get length
print (len(s))

# Replace 
print (s.replace('world, 'everyone'))

# Count
sub = 'h'
print (s.count(sub))

# Starts with
print (s.startwith('hello'))

# End with 
print (s.endwith('d'))

# Split into a list
print (s.split())

# Find position 
print (s.find('r'))

# Is all alphanumeric
print (s.isalnum())

# Is all alphabetic
print (s.isalpha())

# Is all numeric
print (s.isnumeric())
'''

my_school = 'the name of my school is university of abuja'
print(my_school.upper())
print(my_school.lower())
print(my_school.capitalize())
name = 'fortunes'
my_name = 'Fortunes Onyekwere Chimezirim'
print(my_name.upper())
print(my_name.lower())
print(my_name.capitalize())

print(  my_school +' and my name is ' + my_name)

#string formatting

print(f'hello, my name is (my_name)')

#swap case
print(my_name.swapcase())

#get length

print(len(my_name))

#replace
print(my_name.replace('fortunes', 'divine'))

#count
sub = 'e'
print(my_name.count(sub))

#starts with
print(my_name.startswith('Fortunes'))

#ends with
print(my_name.endswith('g'))
print(my_name.endswith('m'))

#split into list
print(my_name.split())

#find position
print(my_name.find('u'))

#is all alphanumeric
print(name.isalnum())

#is all alphabetic
print(name.isalpha())

#is all numeric
print(name.isnumeric())