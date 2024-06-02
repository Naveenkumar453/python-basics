#slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]
# Indexes start with 0 and prints or gets exclusive of stop value.
name = "Naveen Kumar Athelly"
#first_name = name[0]
#first_name = name[0:5]
first_name = name[0:6]
#middle_name = name[8:13]
middle_name = name[7:13]
#sur_name = name[14:]
sur_name = name[13:]
#print(first_name)
#print(middle_name)
#print(sur_name)
#funky_name = name[0:20:1]
#funky_name = name[0:20:2]
#funky_name = name[0:20:3]
#funky_name = name[::3]
#print(funky_name)

# Reverese String
#reversed_name = name[::-1]
#print(reversed_name)
#=====================
#slice function, we can use it for slice and will be used for reusable.
website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])

