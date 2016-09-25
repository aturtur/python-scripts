# functions
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def averageColor(r1,r2,g1,g2,b1,b2):
    calc = (((r1+r2)/2), ((g1+g2)/2), ((b1+b2)/2))
    averageHex = rgb_to_hex(calc)
    return averageHex

# input colors
colorA = "#000000"
colorB = "#ffffff"

# convert
colorA_rgb = hex_to_rgb(colorA)
colorB_rgb = hex_to_rgb(colorB)

# assign
r1 = colorA_rgb[0]
g1 = colorA_rgb[1]
b1 = colorA_rgb[2]
r2 = colorB_rgb[0]
g2 = colorB_rgb[1]
b2 = colorB_rgb[2]

# result
print averageColor(r1,r2,g1,g2,b1,b2)