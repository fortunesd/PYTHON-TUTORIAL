# a function is a block of code that onlt runs when it is called. in python we use identation and not curly bracket

# returns a value

def addNum(num1, num2):
    total = num1 + num2
    return total
print(addNum(20, 8))

def subNum(num1, num2):
    difference = num1 - num2
    return difference
print(subNum(80, 30))

#def sayhelloworld(name= 'fortunes'):
    #print(f'hello {name}')

#print(sayhelloworld('fortunes'))

#lambda function is a small and anonymous function. it can check any number of agurment but can only have in an expression. very similar to the javscript arrow function

addNum = lambda num1, num2: num1 + num2

print(addNum(30, 40))
