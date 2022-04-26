# Makes empty files by given options to script file's location
# 24.04.2022 Arttu Rautio
# https://aturtur/

# Libraries
import os
import platform as pf

# Functions
def GetSep():
    if pf.system() == "Windows": # If os is windwos
        return "\\" # Return \
    else: # Is os is something else (mac or linux)
        return "/" # Return /

def CreateEmptyFiles(fileName, fileRange, zeros, extension):
    path   = os.path.dirname(os.path.realpath(__file__))
    zeros  = int(zeros)
    parse  = fileRange.split("-")
    rStart = int(parse[0])
    rEnd   = int(parse[1]) + 1
    sep    = GetSep()
    for i in range(rStart, rEnd):
        newFilePath = path+sep+fileName+"%s.%s" %(str(i).zfill(zeros), extension)
        makeFile = open(newFilePath, "w")
        print("Created a new file: " + newFilePath)
        makeFile.close()

# Run the program
print ("File name")
fileName = input("> ")

print ("File extension")
extension = input("> ")

print ("File range from-to (example: 5-25)")
fileRange = input("> ")

print ("Zeros (4 = 0001)")
zeros = input("> ")

CreateEmptyFiles(fileName, fileRange, zeros, extension)

print (" ")
print ("Done!")
print (">Exit")