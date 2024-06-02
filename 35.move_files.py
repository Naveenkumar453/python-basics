import os
#source = "test.txt" # To Move a file
#dest = "C:\\Users\\anaveenk\\Desktop\\test.txt"

# To move a directory
source = "python_test_directory" # To Move a file
dest = "C:\\Users\\anaveenk\\Desktop\\python_test"
try:
    if os.path.exists(dest):
        print("There is a already file there")
    else:
        os.replace(source, dest)
        print(source+"was moved")
except FileNotFoundError:
    print(source+"file not found")