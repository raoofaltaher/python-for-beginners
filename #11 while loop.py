# while loop = a statement that will execute its block of code


#while 1==1:
#    print("help i am stuc in this loop! ")

#name = ""
#while len(name) == 0:
#    name = input("Enter your name: ")
#print("Hello " + name)

name = None
while not name:
    name = input("Enter your name: ")
print("Hello " + name)