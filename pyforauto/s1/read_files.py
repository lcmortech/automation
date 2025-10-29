# inputFile = open("inputFile.txt", "r")
# print(inputFile.read()) #READ IS IMPORTANT
# inputFile.close() #bc the method got added to the variable file that was opened

inputFile = open("inputFile.txt", "r")
for line in inputFile:
    line_input = line.split()
    if line_input[2] == "P":
        print(line)
#line_input = [line.split() for line in inputFile if line_input[2] == "P"]
inputFile.close()