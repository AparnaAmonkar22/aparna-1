import os
import re

def renameFileNames(path):

    files = []

    # Find all the CSV files in current directory
    files.extend(i 
                for i in os.listdir(path) 
                # if (i.endswith("csv"))
                )

    a = 1
    # Loop in through each file
    for file in files:
        # Find the file name
        data = re.findall("\w+", file)
        print(data)

        # Check if the filename starts with 'test'
        # if data[0].startswith("test"):

        #Old filename
        old_name = path+file

        # New filename
        new_name = path+"TEST"+str(a)+".csv"

        # Rename old filename with new file name
        os.rename(old_name, new_name)
        a += 1


path = input("Please enter the path: ")
path = path.replace('\\','/')
print(path)

renameFileNames(path)