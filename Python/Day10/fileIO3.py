# with open('fileIO/myfile.txt', "r") as f:
    # f.seek(5)
    # data = f.read(10)
    # current_position = f.tell()
    # f.seek(current_position)
    # data = f.read(12)


# print(data)
# print(current_position)


with open('fileIO/newfile.txt', 'a') as file:
    file.write("Ello mate")
    file.truncate(16)

    with open('fileIO/newfile.txt', 'r') as readFile:
        data = readFile.read()

print(data)