import os
import shutil

#os.remove('test.txt')

# delete file
path = "test1.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("file not found")

# delete empty directory
path1 = "folder"
try:
    os.rmdir(path1)
except FileNotFoundError:
    print("dir not found")
except PermissionError:
    print("you d not have permission to delete that")
else:
    print(path1 + "was deleted")

# delete directory and all files inside
path2 = "folder"
try:
    shutil.rmtree(path2)
except FileNotFoundError:
    print("dir not found")
except PermissionError:
    print("you d not have permission to delete that")
else:
    print(path2 + "was deleted")
