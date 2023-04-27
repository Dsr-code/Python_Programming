# fstrings or fast way to initialize string is a method string formating


'''Earlier we use the traditional way to format string'''
sentance="My name is {} and I am from {}"
name="Devdeep"
place="Saraikela"
print(sentance.format(name , place))

'''But from python 3.6 onwards we use fstring for string formating'''

print(f"My name is {name} and I am from {place}")

# every operation inside the fstring braces is string value

rupee=79.8756655
print(f"One dollar is {rupee: .2f} rupees")     # accepts two decimal value as : this indicates the operation in rupee and .2f means 2 fvalues after(.)


# to view curly braces in fstrings we use another pair of curly braces i,e,

print(f"We use fstrings like this : f\"My name is {{name}} and I am from {{place}}\"")