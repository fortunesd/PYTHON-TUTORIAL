# a set is a collection which is unordered and unindex. No duplicate members

#create a set
colours_set = {'red', 'yellow', 'green', 'white'}

print(colours_set)

#check if in set

print('yellow'in colours_set)
print('black'in colours_set)

# Add to set
colours_set.add('pink')
print(colours_set)

# remove a set
colours_set.remove('pink')
print(colours_set)

# Add duplicate to set
colours_set.add('yellow')
print(colours_set)

# Clear a set
colours_set.clear()
print(colours_set)

# Delete a set
del colours_set
print(Colours_set)
