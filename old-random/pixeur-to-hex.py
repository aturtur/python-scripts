# > python parse pch-file and make it css file
import sys, os
import struct

colors = []
fn = sys.argv[1]
f = open(fn.decode("utf-8"))
def rgb2hex(rgb):
    return struct.pack('BBB',*rgb).encode('hex')
for line in f:
    if line.startswith("R"):
        line = line.split(" ")
        r = line[0][2:]
        g = line[1][2:]
        line = line[2].split(",")
        b = line[0][2:]
        color = rgb2hex((float(r), float(g),float(b)))
        colors.append(color)
f.close()
fo = open(os.path.dirname(os.path.realpath(__file__))+'./colors.css', 'a')
for c in colors:
  fo.write("#%s;\n" % c)

fo.close()