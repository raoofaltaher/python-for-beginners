import os

path = "C:\\Users\\pc\\Desktop\\text.txt"

if os.path.exists(path):
    print("this location exists ")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("this is a directory ")
else:
    print("this location doesnt  exists ")
