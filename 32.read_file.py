#if we wrote program with open to handle files it will autpmatically close the file
# only problem with this is it does not handle exceptions which occur file running like
# cannot locate the file.
# with open('C:\\Users\\anaveenk\\Desktop\\file.txt') as file:
#     print(file.read())
# print(file.closed) #this will check if the file is closed or not
#program if file does not exists
#with open('C:\\Users\\anaveenk\\Desktop\\file.tx') as file: #got error here hence trying try, exec
try:
    with open('C:\\Users\\anaveenk\\Desktop\\file.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file is not found")