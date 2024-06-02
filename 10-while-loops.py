#while loop executes its block of code as long as its conditions remains true.

# while 1==1:
#     print("I am stuck in a loop, help me to come out")

# name = ""
# while len(name)==0:
#     name = input("Enter your name: ")
# print("Your name is "+name)

name = None
while not name:
    name = input("Enter your Name: ")
print("Your name is "+name)