#str.format = is optional menthod that gives users more control when displaying output

#animal = "cow"
#item = "moon"
#print("The "+animal+" "+"jumped over the "+item)
# print("the {} jumped over the {}".format(animal,item))
# print("the {1} jumped over the {0}".format(animal, item)) #possitional parameters
# print("the {0} jumped over the {1}".format(animal, item))
#print("the {animal} jumped over the {item}".format(animal="Cow", item="Moon"))# Keyword argument pairs
#print("the {animal} jumped over the {animal}".format(animal="Cow", item="Moon"))# Keyword argument pairs

# animal = "cow"
# item = "moon"
# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# #padding
# name = "Naveen"
# print("My name is {}".format(name))
# #print("Hello my name is {:10}. Nice to meet you".format(name))
# print("Hello my name is {:>10}. Nice to meet you".format(name))
# print("Hello my name is {:<10}. Nice to meet you".format(name))
# print("Hello my name is {:^10}. Nice to meet you".format(name))
# print("Hello my name is {0:^10}. Nice to meet you".format(name))

number = 4.01567
print("The number pi is {:.2f}".format(number))
print("The number pi is {:.3f}".format(number))

number = 1000
print("The number is {}".format(number))
print("The number is {:,}".format(number)) #to have comma's
print("The number is {:b}".format(number)) #To print binary formar
print("The number is {:X}".format(number)) #To print Hexa Decimal format
print("The number is {:E}".format(number)) #Scientific number format