# tuples = collection which is ordered and unchangeable
#          used to group together related data

student = ("Raoof", 25, "male")
print(student)
print(student.count("male"))
print(student.index("male"))

for x in student:
    print(x)

if "Raoof" in student:
    print("Raoof is here! ")
