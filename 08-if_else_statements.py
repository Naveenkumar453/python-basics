# if statement = a block of code that will execute if its condition is true
age = int(input("how old are you?: "))

if age == 100:
    print("You are a century years old")
elif age >= 18:
    print("you are and adult")
elif age < 0:
    print("You are not born yet")
#elif age == 100: #if statement check step by step age>=18 condintion also matches for this
#    print("You are a century years old")
else:
    print("You are a child")