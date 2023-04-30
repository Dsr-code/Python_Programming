# Note - Import keyword call the module, therefore the file name should not be kept with a module name that can create confusion on importing a module

import math
'''this imports math module through which we can use "math.functions()" (syntax) to use specific functions'''
square= math.sqrt(9)
print(square)    #returns a floationg poiint square root value

from math import pi
'''this type of module calling syntax is used to call specific functions, due to which there is minimun load on the program'''
product=square*pi
print(product)


from math import *
'''this astrics wildcard is used to call all the functions of this module irrespective of a programmer calling those functions or not'''
# this increases the load on the processor as the memory consuption is more

import math as m
'''as keyword is used to alice a name (nickname ) to call the module'''
# Now we can write m.sqrt() instead of math.sqrt()

print(dir(math))
'''this "dir"function prints all the constanst and functions associated with the math function'''

'''Type is used for introspection as here'''
print(type(math.sqrt))  #class <built_in_function_or_method>
print(type(math.pi))    #class <float>


# note- you can import your files as module through the import keyword and that is the reason file name should not be given in the name of module name