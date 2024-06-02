# **kwargs (Key word arguments) is parameter the will pack all arguments into a dictionary
# usefull so that a function can accept a varying amount of keyword argument.
#def hello(first, last):
#def hello(**kwargs):
def hello(**names):
    #print("hello "+first+ " "+ last)
    #print("hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key,value in names.items():
        print(value, end=" ")

hello(title="Mr.",first="Naveen", middle="Athelly", last="Kumar")