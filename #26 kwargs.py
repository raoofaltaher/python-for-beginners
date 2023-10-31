# **Kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varing amount of keyword arguments


def hello(**kwargs):
    #print("Hello", + kwargs['first'], " "+ kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")


hello(first="Raoof", middle="Hayder", last="Altaher",age="25")
