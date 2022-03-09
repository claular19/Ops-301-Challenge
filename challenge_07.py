#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable

file_path = input("Enter a file path: ")

# Declaration of functions

### Declare a function here

for (root, dirs, files) in os.walk(file_path):
    ### Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)
    print('*' * 25)
# Main

### Pass the variable into the function here

os.walk(file_path)

# End
