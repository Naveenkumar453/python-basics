# list is used to store multiple items in single variable
food = ["Dosa", "Idly", "biryani", "cake"]
food[0]= "sushi"
food.append("ice cream")
food.remove("Idly")
food.pop() # removes lost sting
food.insert(0,"idly")
food.sort()
#food.clear()
for i in food:
    print(i)