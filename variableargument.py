averageinput = []
for i in range(5):
    k = int(input("Enter your number :  \n"))
    averageinput.append(k)

print(averageinput)
numbers= tuple(averageinput)
# print(type(numbers))

def average(numbers):
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum+i
    avrge = sum/len(numbers)
    return avrge
v=average(averageinput)
print(v)


# list1=[1,2,3,4,5]
# print(type(list1))

# tup=tuple(list1)
# print(type(tup))
# add=0
# for i in averageinput:
#     add=(add+i)/5
    
    

# print(add)