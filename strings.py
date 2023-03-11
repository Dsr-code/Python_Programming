                #STRINGS
'''one of the most commonly used data types
and Index always starts from 0'''

# name= "Devdeep"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print("\n")
# iterating elements of the "name " using for loop

# for i in name:
#     print(i)

                # String Slicing

'''Its a data seperation type which helps to seperate your desire output'''

fruit= ("Mango")
print (len(fruit))
#len() is a inbuilt function which gives the length of the output


'''() - parenthesis is used for functions
While [] - brackets are used for string slicing'''

# Lets do some string slicing


print(fruit[0:5])
print(fruit[0:4])
print(fruit[0:3])
print(fruit[0:2])
print(fruit[0:1])
print(fruit[0:0])
print(fruit[:])

'''[index from where you want to start : index where you want to end so this one not included]'''
'''when you dont want give any index this takes
first index as - 0 
last index as - len(variable)'''

# Negative Slicing


print(fruit[0:-3])

# this is same as 

print(fruit[0:len(fruit)-3])

print(fruit[-4:-3])

# It automatically subtracts fron the length of the variable - Negative Slicing
