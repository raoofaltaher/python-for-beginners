# keyword arguments = arguments proceeded by an identifier when we
#                     pass them to a function in order of the arguments
#                     doesn't matter, unlike positional arguments python knows the names of the
#                     arguments that our function receives


def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="altaher", first="raoof", middle="hayder")
