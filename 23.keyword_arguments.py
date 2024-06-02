#Keyword Arguments
#arguments preceded by an identifier when we pass them to a function.
# The order of the argument's does not matter, unlike positional arguments.
# Python knows the names of the arguments that our function receives.

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)
#hello("Naveen", "Dude", "code")
#hello("Dude", "code", "Naveen",)
hello(middle="Dude", last="code", first="Naveen",)