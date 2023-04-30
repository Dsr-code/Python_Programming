
def func1():
    pass
def func2():
    pass


if __name__=="__main__":
    func1()
    func2()

print(__name__)  #this will return __main__ as this is the main file to handle the code for the functions func1 and func2, instead it will return the <file name> if imported from other file.py as module

'''if __name__==__main''' # idiom is a common pattern used in python to determine that the code is being run directly or being imported from another file.

'''If we call a file as module from another file the codes of the file being used as module will be auto executed, so to prevent this we keep the fucations under the idiom, and are executed as we call the methods'''