# task 1 - printing single object

print(12312314)
print(4.23532545645)
print((13645-7j))
print('Hello?')
print(True)

# task 2 - printing type of given value

print(type(12312314))
print(type(4.23532545645))
print(type((13645-7j)))
print(type('Hello?'))
print(type(True))

# task 3 - checking type of value

print(isinstance(12312314,int))
print(isinstance(4.23532545645,bool))
print(isinstance((13645-7j),complex))
print(isinstance('Hello?',str))
print(isinstance(True,float))

# task 4 - checking type of value (version 2)

print('Is 123 an instance of int?:', (isinstance(12312314,int)))
print('Is 43.23 an instance of bool?:', (isinstance(4.23532545645,bool)))
print('Is (4-1j) an instance of complex?:', (isinstance((13645-7j),complex)))
print('Is True an instance of bool?:', (isinstance(True,bool)))
print("Is 'How are you?' an instance of float?:", (isinstance('Hello?',float)))

# task 5 - using comments in code


# Block comments ate indented to the same level as that code
a = 45
b = 34
def add(a, b):
    """Blar Blar Blar"""
    return a + b

# print(help(add))

"""
You can use triple-quoted string. When they're not a docstring 
(the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!
"""

abc = None

print(type(abc))

de = 'None'

print(type(de))

print("You can", "use triple-quoted string.", "When they're", "not a docstring", 
      sep="----", end='-------\n')