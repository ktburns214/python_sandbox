# Python has functions for creating, reading, updating, and deleting files.

#open a file
myFile = open("myfile.txt", "w")

# get info on the file
print("name: ", myFile.name)
print("is closed: ", myFile.closed)
print("opening mode: ", myFile.mode)

# write to file
myFile.write("Hello world!")
# can keep appending to file, as above
myFile.close()

# append to file
myFile = open("myfile.txt", "a")
myFile.write("  This is part of the Python crash course")
myFile.close()

# read from file
myFile = open("myfile.txt", "r+")
text = myFile.read(100)
print(text)
