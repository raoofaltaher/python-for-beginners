# Copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file`s creation and motification times)


import shutil
# copy the file to same location
shutil.copyfile('text.txt', 'copy.txt') #src.dst

# copy the file to other location by put the location path and name of the file instead of just the file name

shutil.copyfile('text.txt', 'C:\\Users\\pc\\Desktop\\copy.txt') #src.dst