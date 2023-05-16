'''There are some functions of FileIO which makes it more easy to work with the files '''

# with open('rough.txt','r') as f:
#     for line in f.readlines():
#         print(line)

    # readline() function helps to print the llines in the file with the format of list and can be easily iterated with the help of for loop


f=open("marks.txt","r")
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    m1=line[0]
    m2=line[1]
    m3=line[2]
    print(f"marks of roll{i} in Maths is {m1} ")
    print(f"marks of roll{i} in physics is {m2}")
    print(f"marks of roll{i} in chemisty is {m3}")
    print(line)
# f.close()

print(f.readline())
content= f.read()
print(content)