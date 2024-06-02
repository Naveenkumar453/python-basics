#tuples = collections which is ordered and unchangeble
# used to group together related data.
student = ("Naveen", 33, "Male")
print(student.count("Naveen"))
print(student.index("Male"))
for x in student:
    print(x)

if "Naveen" in student:
    print("Naveen is here")