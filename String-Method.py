                # String Methods
'''Strings are immutable so when you change a sting variable it creates another variable copy'''
# Some most commonly and important used methods for strings

a = "devdeep singh rajput !!!"
print(a)
print(len(a))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # strips the trailling charecters given
print(a.replace ("devdeep", "amardeep")) #replaces all the occurances
print(a.split(" ")) #returns a list of items sepereted by space as argument here is space
print(a.center(24))
print(a.count("devdeep"))
print(a.endswith("!")) #returns a Boolean
print(a.endswith("singh",8,13)) #returns a Boolean if found between index 8 to 13 if returns -1
print(a.find("gh")) #returns -1 if donot match
print(a.index("h")) #return valueError if donot match
print(a.isalnum()) #Returns TRUE if the string is alphanumeric(i.e, A_Z,a-z,0-9)
print(a.isalpha()) # return true if string is alphabet
'''Many more like-wise functions exists like 
(isascii, isdecimal, is digit, isidentifier,   islower, upper, numeric, printable, )'''
print(a.join(""))
print(a.rfind("singh")) #Finds the index where the word starts
print(a.split("-")) #splits the items with the hyphen as here given here
print(a.startswith("s")) #returns true if the string startswith letter mentioned
print(a.splitlines()) #splits the string where the line breaks
print(a.swapcase()) #swaps the upper case into lower case
print(a.title()) #converts the first charecter to upper case of each elemant of the string