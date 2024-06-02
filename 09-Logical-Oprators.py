#Logical Operators (and, or, not) is used to check when two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30: #Here both conditions should satisfy
#     print("The temperature is good today")
#     print("Go Outside")
# elif temp < 0 or temp > 30: #One condition can be true
#     print("The temperature is bad today")
#     print("stay inside")

#Not Operators can be used with one or more condidtional statements
if not(temp >= 0 and temp <= 30): #Here both conditions should satisfy
    print("The temperature is bad today")
    print("stay inside")
elif not(temp < 0 or temp > 30): #One condition can be true
    print("The temperature is good today")
    print("Go Outside")