# python has functions for creating, reading, updating anf delecting a file

#open a file

fortunesFile = open('chimezirim.txt','w')

# Get information

print('Name:', fortunesFile.name)
print('is closed:', fortunesFile.closed)
print('opening mode:', fortunesFile.mode)

# Write to file
fortunesFile.write('fortunes is my english name')
fortunesFile.write(' i am from Abia state')
fortunesFile.close

# Append to file
fortunesFile = open('chimezirim.txt', 'a')
fortunesFile.write(' i also leaving in abuja nigeria and i love python')
fortunesFile.close

# reading from file

fortunesFile = open('chimezirim.txt', 'r+')
text = fortunesFile.read(100)
print (text)

