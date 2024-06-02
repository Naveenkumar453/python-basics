# exception = events detected during execution that interrupt the flow of the program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    #print(result)

except ZeroDivisionError as e:
    print(e) #to print the exception
    print("You can't divide by Zero")
except ValueError as e:
    print(e)
    print("Enter only numbers pls")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("This will always execute.") #good option to use open and close files