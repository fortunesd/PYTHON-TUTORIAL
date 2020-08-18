# If/Else conditions are used to decide something based on the condition being true or false

age_casmir = 17
age_abdul = 16


# Comparison operators(==, !=, >, <,) = used to compare values

# Single if
if age_casmir > age_abdul:
    print(f'{age_casmir} is greater than {age_abdul}')

# If/Else

if age_casmir > age_abdul:
    print(f'{age_casmir} is greater than {age_abdul}')
else:
    print(f'{age_abdul} is greater than {age_casmir}')

# Elif

if age_casmir > age_abdul:
    print(f'{age_casmir} is greater than {age_abdul}')
elif age_casmir == age_abdul:
     print(f'{age_abdul} is equal to {age_casmir}')
else:
     print(f'{age_abdul} is greater than {age_casmir}')

#nested if
if age_casmir > 10:
    if age_casmir <= 20:
        print(f'{age_casmir} is greater than 10 and less than or equal to 20')

# Logical operators ( and, or ,not) used to combine conditionals statements

# And operators

if age_casmir > 10 and age_casmir <= 20:
    print(f'{age_casmir} is greater than 10 or less than or equal to 20')

#or operators
if age_casmir > 10 and age_casmir <= 20:
    print(f'{age_casmir} is greater than 10 or less than or equal to 20')

# if not
if not(age_casmir == age_abdul):
    print(f'{age_casmir} is not equal to {age_abdul}')

# membership operators (in, not in) membership operators are used to test if a squence is present in an object
ages = [19, 20, 20, 18, 19, 20]

# in
if age_casmir in ages:
    print(age_casmir in ages)

# not in
if age_casmir not in ages:
    print(age_casmir not in ages)

# identity operators (is, is not) compare the objects, not if they are equal, but if they are actually the same time of object, with the same memory location

# is
if age_casmir is age_abdul:
    print(age_casmir is age_abdul)

# is not
if age_casmir is not age_abdul:
    print(age_casmir is not age_abdul)




