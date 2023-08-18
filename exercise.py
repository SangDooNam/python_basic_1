# task 1 - printing single object

print(123)
print(43.23)
print((4-1j))
print('How are you?')
print(True)

# task 2 - printing type of given value

print(type(123))
print(type(43.23))
print(type((4-1j)))
print(type('How are you?'))
print(type(True))

# task 3 - checking type of value

print(isinstance(123,int))
print(isinstance(43.23,bool))
print(isinstance((4-1j),complex))
print(isinstance('How are you?',str))
print(isinstance(True,str))

# task 4 - checking type of value (version 2)

print('Is 123 an instance of int?:', (isinstance(123,int)))
print('Is 43.23 an instance of bool?:', (isinstance(43.23,bool)))
print('Is (4-1j) an instance of complex?:', (isinstance((4-1j),complex)))
print('Is True an instance of bool?:', (isinstance(True,bool)))
print("Is 'How are you?' an instance of float?:", (isinstance("How are you?",float)))

# task 5 - using comments in code

# This is my first comment
# Block comments ate indented to the same level as that code

print("Hello")
print("Line with inline code!") # remember about spacing!

print(type(123.45)) # getting type of number

"""
You can use triple-quoted string. When they're not a docstring (the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!
"""