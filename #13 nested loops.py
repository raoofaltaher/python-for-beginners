# nested loop = in general it is a loop inside loop
#               the "inner loop" will finish all of its iterations befor
#               finish ine iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

    