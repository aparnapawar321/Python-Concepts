
pFile = open("pythonTheory.txt")
print("*"*20, "\nFile reading\n","*"*20, pFile.read())

#use if with
with open("pythonTheory.txt") as f:
    print("*"*20, "\nFile reading when used with\n","*"*20, f.read)

#readline and file close()
with open("pythonTheory.txt") as f:
    print("*"*20, "\nreadline and close use\n","*"*20, f.readline())
    f.close()

#read part of file
file = open("pythonTheory.txt")
print("*"*20, "\nPart of file reading\n","*"*20, file.read(6))

#Append the content to file
with open("pythonTheory.txt", "a") as f:
    f.write("Now the file has more content!")
with open("pythonTheory.txt") as f:
    print(f.read())

#overwrite the content, use "w"
with open("pythonTheory.txt", "w") as f:
    f.write("oops! I've deleted the content")
with open("pythonTheory.txt") as f:
    print(f.read())

#Create a new file called "myfile.txt", returns an error if the file exists
f = open("myfile.txt", "x")

#To delete a file, you must import the OS module, and run its os.remove() function
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")
