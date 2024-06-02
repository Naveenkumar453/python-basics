import os
#need to one more \ if \ already exists as \ represents new line

#path = "C:\\Users\\anaveenk\\Desktop\\file.txt"
path = "C:\\Users\\anaveenk\\Desktop\\file"
if os.path.exists(path):
    print("The location exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("That is directory")


else:
    print("The location doesn't exists")