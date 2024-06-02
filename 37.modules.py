#module is file containing python code. May contain functions, classes, etc
# used with modular programming, which is to seperate program into parts.
#import messages
#messages.hello()
#messages.bye()
#===========
#import as
# import messages as msg
# msg.bye()
# msg.hello()
#=================
# import messages functions only
#from messages import hello,bye
#hello()
#bye()
#Larger porgrams don;t use this as it uses lot of functions can be duplicated also
#we can refer python modules
from messages import *
hello()
bye()
# to list all the modules
help("modules")
