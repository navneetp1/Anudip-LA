filename = input("Enter a filename with some extension(eg: abc.txt): ") 
f = open(filename, "w")
f.write("Some input has been entered.")

f.close()