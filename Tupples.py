
        # Tuples are immutable datatypes
'''To declare a tuple we use a parenthesis or assign values seperated by comas'''


tups=1,2,
print(type(tups))
print(len(tups))



tup=("Dsr","Saii",143,True)
print(tup[0])

if "Saii" in tup:
    print("yesssssss")
else:
    print("Nooo")

# for i in tup:
#     print(i)
#     for j in i:
#         print(j)    #Int and Boolean are not iterable


'''After slicing a new tuple is gained'''

 

tuple1=(1,2,3,4,5,6,7,8,9)
tupleslice=tuple1.index(3,1,5)
print(tupleslice)