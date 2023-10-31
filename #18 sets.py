# set = collection which is unordered, unindexed. no duplicate values

items = {"fork", "spoon", "knife"}
# items.add("napkin")
# items.remove("fork")

dishes = {"bowl", "plate", "cup", "knife"}

#items.update(dishes)

#dinner_table = items.union(dishes)
#for x in dinner_table:
#    print(x)

print(dishes.difference(items))
print(items.intersection(dishes))