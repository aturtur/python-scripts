# Frame calculator
#############################################################################
print ("Frames?")										# Question
frameRange = raw_input(">")								# Frame range input

print ("Frame rate?")									#Question
fps = float(raw_input(">"))								# Frame rate input

mode = frameRange.count("-")

if mode == 1:
	parse = frameRange.split("-")						# Parse input
	rStart = float(parse[0])							# Get first frame
	rEnd = float(parse[1])								# Get last frame
	fRange = rEnd - rStart								# Calculate range length
else:
	fRange = float(frameRange)							# No range, just frames

time = fRange / fps										# Calculate time
seconds = int(time)										# Seconds
frames = fRange - (seconds*fps)							# Glut frames
#############################################################################
print ("")

if seconds > 0 and frames > 0:
	print (str(int(fRange)) + " frames @ " + str(int(fps)) + " FPS")	
	print (str(int(time)) + " seconds and " + str(int(frames)) + " frames")
elif seconds > 0:
	print (str(int(fRange)) + " frames @ " + str(int(fps)) + " FPS")	
	print (str(int(time)) + " seconds")
else:
	print (str(int(fRange)) + " frames @ " + str(int(fps)) + " FPS")	
	print (str(frames) + " frames")
print (">Exit")