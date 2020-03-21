# First I need to get file names from a folder
# Then I should change names of every file

import os

def rename_files():
    # find file's name
    filenames = os.listdir(os.getcwd() + '/files')

    # Change the file name
    for filename in filenames:
        os.rename(filename, "Happy")        
        print(filename)
       

rename_files()