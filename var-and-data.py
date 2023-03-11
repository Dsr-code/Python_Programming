

                # EVERYTHING IN PYTHON ARE OBJECTS #
                     # AND ARE CASE SENSITIVE #

# Data types in python
''' 1. String
            :Any alphabaticsl word that is supposed to be stored in a variable is termed as String'''

a = "Devdeep"
print (a)
print(type(a))

'''2. Numbers
            :Numbers are best known by it's name that the data represented in the form of any Number'''
#Interger
b = 100
print(b)
print(type(b))

# Float -(decimal format of numbers)
c = 1.2
print(c)
print(type(c))

'''3. Boolean
            :Boolean basically stores TRUE or FALSE where 0 is represented as Flase and True as 1'''
t = True
print(type(t))

'''4. List
            :List is basically a collection of datatype or datas enclosed by square-brackets[] and are mutable'''
list1 = [ "devdeep","saii", 143, [1,2,3], True]
print(list1)
print(type(list1))

'''5. Tupple
            :Same as List but Tupples are immutable unlike Lists and are enclosed by paranthesis() '''
tup1 = (12, 5, "love", ("apple", "orange"))
print(tup1)
print(type(tup1))

'''6. Dictionary
            : Dictionaries are the datatype which holds the data as a "key":"value" pair and are enclosed by curly-braces'''
dict1 = {"name": "dev", "age":20 , "canVote":True}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1["name"])
print(dict1.get("canVote"))
print(type(dict1))



