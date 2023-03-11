# Docstrings are the special type of strings which are used to define or instruct the progammer about the program

def square(n):
    '''Enter numbers to get the square of the number you have entered'''
    return n**2

print(square(9))
print(type(square.__doc__))

