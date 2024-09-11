f = open("newfile.txt", "r")

while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = open("myfile.txt", "a")
# lines = ["line 1\n", "line 2\n", "line 3\n"]
lines = ["line 1", "line 2", "line 3"]
for line in lines:
    f.write(line + '\n')

f.close()

with open("myfile.txt", "r") as file:
    print(file.read())