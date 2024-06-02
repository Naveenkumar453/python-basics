#nested function calls are function calls inside another function calls
#inner most functions are resolved first
#returned value is used as argument for the next outer function
# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("enter a whole positive number ")))))