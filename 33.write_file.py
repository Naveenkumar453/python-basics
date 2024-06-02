
#text = "Hello\nGood Morning\nHow are you doing"
#text = "Checking if this overwrites previous text"
# with open('test.txt', 'w') as file:  #w is to write to a file, this is overwritten when second text given
#     file.write(text)
text = "\nChecking with 'a' for appending"
with open('test.txt', 'a') as file: #a is used for appending
    file.write(text)