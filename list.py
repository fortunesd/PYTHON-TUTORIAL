#list is a collection which is ordered and chanagable allow duplicate

#create list

ages = [2, 20, 6, 40, 50, 89, 3]

colours = ['red', 'yellow', 'green', 'grey']

#use a construtor

ages2 = list((10, 20, 35, 40, 50))

print(ages)
print(ages2)

# get a value
print(colours[2])

# Get length 
print(len(colours))

#append to list
colours.append('white')
colours.append('black')

print(colours)

#remove from list
colours.remove("red")
print(colours)

#insert into a particular position
colours.insert(3, "blue")
print(colours)

#change a value
colours[1] = 'pink'
print(colours)

#remove with pop
colours.pop(2)
print(colours)

#reverse list
colours.reverse()
print(colours)

#sort a list
colours.sort()
print(colours)
ages.sort()

print (ages)

#reverse sort
ages.sort(reverse=True)
print(ages)

