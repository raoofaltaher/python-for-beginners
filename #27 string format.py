# Str.format() = optional method that gives users more control when displaying output


#animal = "cow"
#item = "moon"

#print("the {} jumped over the {}".format(animal, item))
#print("the {1} jumped over the {0}".format(animal, item)) #positional argument
#print("the {animal} jumped over the {item}".format(animal="cow", item="moon")) #keyword argumwnt

#text = " the {} jumped over {}"
#print(text.format(animal, item))


#name = "Raoof"
#print("Hello, mu name is {}".format(name))
#print("Hello, mu name is {:<10}.nice to meet you".format(name))
#print("Hello, mu name is {:>10}.nice to meet you".format(name))


number = 3.141590
print("the number pi is {:.3f}".format(number))
print("the number pi is {:.2f}".format(number))
print("the number pi is {:,}".format(number))
print("the number pi is {:x}".format(number))
