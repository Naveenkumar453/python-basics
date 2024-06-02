# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

#def add(num1,num2):
# def add(*args):
def add(*stuff):
    sum = 0
    stuff = list(stuff)  # tuple does not support item assignment hence converting into to list
    stuff[0] = 0          #assigning here.
    for i in stuff:
        sum += i
    return sum
print(add(1,2,3,4,5,6))