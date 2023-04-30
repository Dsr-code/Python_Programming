marks = [12,23,45,55,62,40,88,95]


# for mark in marks :
#     index = 0
#     print(mark)
#     if index == 2:
#         print("Index is two")
#         index+=1

'''Enumerate function helps to get index with respect to the value in the list, '''

# It returns index starting from 0 ,(coma) value in the for loop  to iterate the items in the list

for index, mark in enumerate(marks):
    print(mark)
    if index == 2:
        print("Very Nice")
        