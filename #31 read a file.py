with open('text.txt') as file: #or the file path
    print(file.read())
#print(file.closed)

# if i miss writing the file name this is a better way to wrte the code
try:
    with open('text.tx') as file: #or the file path
        print(file.read())
except FileNotFoundError:
    print("this file was not found ")