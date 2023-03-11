inp1 = int(input("Enter the number\n"))
inp2 = int(input("Enter another number\n"))
print("\n1 for add\n 2 for sub \n 3 for mul \n 4 for div")
opp = input(print("enter the operator, "))

if opp == 1:
    print ("Result\n ", inp1 + inp2)
elif opp == 2:
    print ("Result\n ", inp1 - inp2)
elif opp == 3:
    print ("Result\n ", inp1 * inp2)
elif opp == 4:
    print ("Result\n ", inp1 / inp2)
else:
    print ("invalid input")


# a = int(input("enter a no\n"))
# b = int(input("enter another no"))

# print(a+b)




