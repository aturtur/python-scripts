# render time calculator
from datetime import datetime, timedelta

# how many frames
print ("How many frames?")
frames = (raw_input(">"))
print("")
print ("Render time per frame? Input time hh:mm:ss")
ftime = raw_input(">")
if "-" in frames:
    f_range = frames.split("-")
    s_range = int(f_range[0])
    e_range = int(f_range[1])
    frames = int(e_range - s_range)
else:
    frames = int(frames)    
mode = ftime.count(":")
parse = ftime.split(":")

# mode hh-mm-ss
if mode == 2:
    hours = int(parse[0])
    minutes = int(parse[1])
    seconds = int(parse[2])

    htime = hours*60*60
    mtime = minutes*60
    stime = seconds    
    render_time = (htime + mtime + stime)*frames

    sec = timedelta(seconds=int(render_time))
    d = datetime(1,1,1) + sec
    print("")
    print("Rendering %d frames takes:\n%d days, %d hours, %d minutes, %d seconds" % (frames, d.day-1, d.hour, d.minute, d.second))
# mode mm-ss
elif mode == 1:
    minutes = int(parse[0])
    seconds = int(parse[1])

    mtime = minutes*60
    stime = seconds
    render_time = (mtime + stime)*frames

    # result
    sec = timedelta(seconds=int(render_time))
    d = datetime(1,1,1) + sec
    print("")
    print("Rendering %d frames takes:\n%d days, %d hours, %d minutes, %d seconds" % (frames, d.day-1, d.hour, d.minute, d.second))

# mode ss
elif mode == 0:
    stime = int(parse[0])
    render_time = stime*frames

    # result
    sec = timedelta(seconds=int(render_time))
    d = datetime(1,1,1) + sec
    print("")
    print("Rendering %d frames takes:\n%d days, %d hours, %d minutes, %d seconds" % (frames, d.day-1, d.hour, d.minute, d.second))

# end
void = raw_input(">Exit");