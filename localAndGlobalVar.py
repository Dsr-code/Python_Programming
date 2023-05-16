x= 5
y=4

def changeVar():
    global x        #global keyword allows the function to change the global value in local operations
    x+=10
    return x
changeVar()
print(x)


'''Local Scope variable is a variable defined only inside the function and we cannot access the variable from global scope'''

'''Global Scope variable is a variable which can be accessed from all over the program '''


