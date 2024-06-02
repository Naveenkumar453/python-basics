#copyfile() = copies content of a file
#copy() = copyfile() + permission mode + destination can be directory
#copy2() = copy() + copies meta deta (file creation and modification time)
import shutil
#shutil.copyfile('test.txt', 'copy.txt') #src, Dest
shutil.copy('test.txt', 'C:\\Users\\anaveenk\\Desktop\\file')
shutil.copy2('test.txt','C:\\Users\\anaveenk\\Desktop\\file')