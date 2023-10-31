# slicing = create a substring by extracting elements from another
#    indexing[] or slice()
#    [start:stop:step]

name = "Raoof hayder"
#first_name = name[4]

first_name = name[0:5]
last_name = name[6:12]
funky_name = name[0:12:2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])

