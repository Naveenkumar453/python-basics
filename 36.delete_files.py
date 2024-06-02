import os
import shutil
#path = "test.txt" #testing locall files within project
#path = "C:\\Users\\anaveenk\\Desktop\\test.txt" #test with files
#path = "C:\\Users\\anaveenk\\Desktop\\test_folder" #test with directories
#path = "C:\\Users\\anaveenk\\Desktop\\folder" #testing with directories which have files
try:
    #os.remove(path)  #to remove/delete files
    #os.rmdir(path)     #delete an empty directory
    shutil.rmtree(path) #delete a files including files in it
except FileNotFoundError as e:
    print(e)
    print(path+" file was not found in the path")
except PermissionError as e:
    print(e)
    print("You don;t have permission to delete that")
except OSError as e:
    print(e)
    print("You cannot delete that function, try shutil module")
else:
    print(path+" was deleted successfully")
