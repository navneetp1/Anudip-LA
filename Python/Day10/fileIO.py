# file = open("myfile.txt", "a")
# file.write("gayge") 

# file.close()

# newFile = open("myfile.txt", "r")
# textContent = newFile.read()
# print(textContent)

# newFile.close()


# shortcut method
with open("newfile.txt", "w") as textFile:
    textFile.write("Hindi is gone now you check again by repoening the file")

with open("newfile.txt", "r") as modifiedFile:
    content = modifiedFile.read()

print(content)

