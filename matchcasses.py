                    # Match Case
'''IF your python version is 10 or above you can use these match cases. Match cases are basically logic which matches the value of the 'match' with the no. of cases you defined in the program. '''

a = int (input("Enter the value : "))

match a :
    case 0:
        print("The  value is neutral")
    case -1:
        print("The value you entered is Negative")
    case 1 :
        print("The value you entered is Positive")
    case _:
        print("Not a signum functions output")
        