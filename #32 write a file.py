text = "Helloooo raoof\nthis is new line\nHave a good day"

# this will over write the current file
with open('text.txt', 'w') as file:
    file.write(text)
# this will NOT over write the current file
with open('text.txt', 'a') as file:
    file.write(text)