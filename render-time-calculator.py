# Render time calculator
from datetime import datetime, timedelta
#########################################################
# How many frames
print ("How many frames?")								# Question
frames = (raw_input(">"))								# Frames input
print("")
print ("Render time per frame? Input time hh:mm:ss")
ftime = raw_input(">")									# Render time input
if "-" in frames:
	f_range = frames.split("-")
	s_range = int(f_range[0])
	e_range = int(f_range[1])
	frames = int(e_range - s_range)
else:
	frames = int(frames)	
mode = ftime.count(":")									# Get right mode from counting dashes
parse = ftime.split(":")								# Parse input
#########################################################
# Mode selection
if mode == 2:											# Mode hh-mm-ss
	hours = int(parse[0])								# Get hours
	minutes = int(parse[1])								# Get minutes
	seconds = int(parse[2])								# Get seconds

	# Convert render times to seconds
	htime = hours*60*60									# Hours in seconds
	mtime = minutes*60									# Minutes in seconds
	stime = seconds 									# Seconds in seconds

	# Calculate some stuff
	render_time = (htime + mtime + stime)*frames		# Add everything together

	# Results
	sec = timedelta(seconds=int(render_time))
	d = datetime(1,1,1) + sec
	print("")
	print("Rendering %d frames takes:\n%d days, %d hours, %d minutes, %d seconds" % (frames, d.day-1, d.hour, d.minute, d.second))
#########################################################
elif mode == 1:											# Mode mm-ss
	minutes = int(parse[0])								# Get minutes
	seconds = int(parse[1])								# Get seconds

	# Convert render times to seconds
	mtime = minutes*60									# Minutes in seconds
	stime = seconds 									# Seconds in seconds

	# Calculate some stuff
	render_time = (mtime + stime)*frames 				# Add everything together

	# Results
	sec = timedelta(seconds=int(render_time))
	d = datetime(1,1,1) + sec
	print("")
	print("Rendering %d frames takes:\n%d days, %d hours, %d minutes, %d seconds" % (frames, d.day-1, d.hour, d.minute, d.second))
#########################################################
elif mode == 0:											# Mode ss
	stime = int(parse[0])								# Get seconds

	# Calculate overall render time
	render_time = stime*frames							# Add everything together

	# Final calculation and print results
	sec = timedelta(seconds=int(render_time))
	d = datetime(1,1,1) + sec
	print("")
	print("Rendering %d frames takes:\n%d days, %d hours, %d minutes, %d seconds" % (frames, d.day-1, d.hour, d.minute, d.second))
#########################################################
# End
void = raw_input(">Exit");