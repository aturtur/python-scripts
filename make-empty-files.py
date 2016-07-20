import os
path = os.path.dirname(os.path.realpath(__file__))

print ("Frame name (remember to put also separator!)")
fileName = raw_input(">")

print ("Files (example: 0-100)")
fileRange = raw_input(">")

print ("Zeros (4 = 0001)")
zeros = raw_input(">")

print ("File extension")
type = raw_input(">")

zeros = int(zeros)
parse = fileRange.split("-")
rStart = int(parse[0])
rEnd = int(parse[1]) + 1
for i in range(rStart, rEnd):
    makeFile = open(r""+path+"\\"+fileName+"%s.%s" %(str(i).zfill(zeros), type), "w")

print (" ")
print ("Done!")
print (">Exit")