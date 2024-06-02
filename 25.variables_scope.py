# scope is the region that variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created.
#LEGB rule Local Enclosing Global built-in
name = "Naveen" #global scope (available inside and outside function)
def display_name():
    #name = "Kumar"   #local scopt (available only inside the function)
    print(name)

display_name()
print(name)
