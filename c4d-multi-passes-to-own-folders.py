# cinema 4d multi-passes to own folders
# NOTE: ATM does not support object buffers
import os
import re

folderPath = r"C:\kansio"

items = []
images = []
folders = set([])

# scan folder
for file in os.listdir(folderPath):
    items.append(file)

for item in items:

    # what folders do we need
    divider = item.rfind('_')
    endPart = item[divider+1:]
    folderName = re.split('(\d.*)',endPart)[0]
    folders.add(folderName)

    # images to array
    #imageName = re.split('(\d.*)',item)[0]
    #images.append(imageName)

# make folders
for item in folders:
    if not os.path.exists(folderPath+"\\"+item):
        os.makedirs(folderPath+"\\"+item)

# copy images to folders
folders = list(folders)
for i in items:
    for f in folders:
        if folders[folders.index(f)] in i:
            os.rename(folderPath+"\\"+i, folderPath+"\\"+folders[folders.index(f)]+"\\")

#
#print items

# re_pattern = "-*\d+[.]\w+$"
# .rfind('_')
# .split('_')[0]
#newpath = r'C:\Program Files\arbitrary' 
#if not os.path.exists(newpath):
    #os.makedirs(newpath)


#        for (var k = 0; k < audios.length; k++) {
#            if (audios[k] === fileformat) {
#                make_audio = 1;
#}