
#File Handling

# r  -  read-only
# w  -  write-only
# a  -  append-only
# r+ -  read+write
# w+ -  write+read
# a+ -  append+read
# rb -  read binary
# wb -  write binary
# ab -  append binary



# file=open("sample1.txt","w")
# file.write("Hello\n ")
# file.write("Welcome to Sample Page 1")
# file.close()


# file=open("sample1.txt","r")
# content=file.read()
# print(content)
# file.close()

# file=open("sample1.txt","a")
# file.write("This is the new line appended.\n")
# file.close()



# use with in file handling so we dont need to close the file everytime python automatically does them

with open("sample1.txt","r") as file:
    for line in file:
        print(line.strip())







