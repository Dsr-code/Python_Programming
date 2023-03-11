l1=[1,2,3,4,5]
print(l1)
print(type(l1))
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[1 ])
print(l1[0])

# List slicing with colomns
'''list[start:ends:steps_or_jump_index]'''

'''
Start - Include
End - Exclude
'''

print(l1[1:4:2])

# List comphrension 

# Normal syntax for logical list

numbers=[]
for i in range(10):
    square=i*i
    numbers.append(square)

print(numbers)

# comprehension

comprehensionList=[i*i for i in range(10)]
print(comprehensionList)



'''To check a value in a list '''

if 64 in numbers:
    print("Yesss")
else:
    print("No")