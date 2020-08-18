# A for loop is used for iterating over a sequence (that is either a list, a tuple, a set, or a string).

students = ['fortunes', 'abdul', 'obinaka', 'amos', 'ibrahim', 'zaniab']


# simple for loop

for student in students:
    print(f'i am: {student}')

#break
for student in students:
    if student == 'odinaka':
        break
    print(f'the student is: {student}')

#continue

for student in students:
    if student == 'odinaka':
        continue
    print(f'the people included: {students}')

#range
for person in range(len(student)):
    print(f'number: {person}')

# custom range 

for n in range(0, 12):
    print(f'number: {n}')

# while loops excute a set of statements as long as a condition is true.

count = 0
while count < 10:
    print(f'count: {count}')
    count += 1
    