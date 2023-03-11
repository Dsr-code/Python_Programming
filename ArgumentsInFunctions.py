# types of arguments in functions

# Required Arguments
'''No of parameters which is passed in the functions is required arguments when it is compulsory to pass them all '''

def average(a, b):
    avg = (a+b)/2
    return avg
r=average(5,6)
print (r)

'''when we call the function it is necessary to input the Required Arguments'''

# Default Arguments
'''This type of fuctions owns a default value to the parameters if not insrted by the user during calling the functions'''

def average1(a1=10, b1=20):
    avg1 = (a1+b1)/2
    return avg1
d=average1()
d1=average1(5,8)
print (d)
print (d1)

# Keyword Arguments
'''In this type of argument the function accepts value of the parameters where order is not imortant '''
def average2(a2, b2):
    avg2 = (a2+b2)/2
    return avg2
k=average2(b2=5,a2=66)
print (k)

# Variable Length Arguments
'''when you don't know the no of parameters to be passed through the function '''

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum+i
    avrge = sum/len(numbers)
    return avrge
v=average(1,2,3,4,5,6,7,8,9)
print(v)