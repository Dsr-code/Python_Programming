import os

for i in range(10):
    os.mkdir(f"LearnOsModule/data{i}")
# This os.mkdir() method is used to create folders in the given location


for i in range(10):
    os.rmdir(f"LearnOsModule/data{i}")
# This os.rmdir() method is used to remove folders present in the given location

'''There are many methods such as : rename to rename the directories, os.listdir is used to list the content inside the directory etc..'''

                # There are more out to explore 