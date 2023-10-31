# return statement = Functions send python valuse/objects back to the caller.
#                    these values/objects are known as the function`s return value

def multiply(number1,number2):
    result = number1 * number2
    return result
print(multiply(6,8))

x = multiply(5,6)
print(x)

def multiply1(number3,number4):
    return number3 * number4
x = multiply1(6,6)
print(x)