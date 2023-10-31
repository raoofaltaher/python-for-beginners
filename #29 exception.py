# exception = events detected during execution that interrupt the flow of program

try:
   numerator = int(input("Enter a number to divide: "))
   denominator = int(input("Enter a number to divide by: "))
   result = numerator/denominator
   print(result)
except ZeroDivisionError:
    print("You can`t divide by 0 ")
except ValueError:
    print("Enter only numbers ")
except Exception:
    print("Something went wrong :( ")

else:
    print(result)

finally:
    print("This will always execute ")
