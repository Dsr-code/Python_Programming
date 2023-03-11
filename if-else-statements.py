                #Conditional Statements
'''These are the statements used in a program to give the program LOGIC. There are basically 3 conditional operator IF ELIF ELSE '''

num = int(input("Enter a No : "))
if num < 0:
    print("The Number is Negative")
elif num == 0:
    print("Your value is Netural")

else:
    print("The Number is Positive Number")

    if num%2 ==0:
        print("The Number is Even positive number")
    else :
        print("The Number is odd Positive Number")

