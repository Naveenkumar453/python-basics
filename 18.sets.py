#set is a collection which is unordered, unindexed. No duplicate values
# list is faster

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}
#utensils = {"fork", "spoon", "knife","knife","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)

dinner_table = utensils.union(dishes)

#print(utensils.union(dishes))
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
# for x in utensils:
#     print(x)

# for x in dinner_table:
#     print(x)