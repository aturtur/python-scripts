# cinema 4d multi-passes to own folders
import os
import re

fp = r"E:\kansio"

items = []
folders = set([])

# scan folder
for file in os.listdir(fp):
    items.append(file)

# loop items
for item in items:
    # what folders do we need
    divider = item.rfind('_')
    endPart = item[divider+1:]
    folderName = re.split('(\d.*)',endPart)[0]
    folders.add(folderName)

# make folders
for item in folders:
    if not os.path.exists(fp+"\\"+item):
        os.makedirs(fp+"\\"+item)

# copy images to folders
folders = list(folders)
for i in items:
    for f in folders:
        if folders[folders.index(f)] in i:
            oldPath = fp+"\\"+i
            newPath = fp+"\\"+folders[folders.index(f)]+"\\"+i
            os.rename(oldPath, newPath)

print "done"