# f=open('strings.py','r')            #read mode is default
# text=f.read()
# print(text)
# f.close

'''This can be used to work with files with the help of python'''
# syntax
'''make a file pointer and open the file'''
# f=open('fileName','mode')   
'''initialize the content to a variable'''
# text=f.read()
'''print the content and close the file'''
# print(text)
# f.close

'''modes

read - r
write - w
append - a
'''
# Note- If you open a file in write mode and the file does not exists, it will auto create that file

# '''TO WRITE A FILE'''
w=open('rough.txt','w')
w.write("Hey this is a dummy text for the practice of file io write mode\n")
w.close()


f=open('rough.txt','r')
text=f.read()
print(text)
f.close()

# append is used when you want to write something in the file with the previous content available unlike write mode deletes the previous content and writes the new content


'''                                          ANOTHER BEST WAY TO WORK WITH FILEIO                                                               '''

# with open('rough.txt','a') as f:
#     f.write("This is the appended text added to rough.txt")

with open('rough.txt','r') as p:
    lines=p.read()
    print(lines)

    # with keyword auto closes the file
