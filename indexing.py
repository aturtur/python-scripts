# Indexes folder path for comparison operation
# 22.04.2022 Arttu Rautio
# Python 3 or newer

# Libraries
import os
import sys
import re

# ------------- Folder path -------------
# Folder path
path = ""
saveName = "IndexedDirectory.txt"

# File extensions to search (if empty, search all possible)
search_file_types = []

# File extensions to ignore
ignored_file_types = ['.txt', '.inf', '.ini']
# ----------------------------------------

# Functions
def CollectFiles(folder):
    collectFiles = {}
    i = 0
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            path = subdir+"/"+file
            fn, fe = os.path.splitext(path)
            dot = re.search("^\.\w+", file)
            if not dot:
                if fe.lower() not in ignored_file_types:
                    if len(search_file_types) != 0:
                        if fe.lower() in search_file_types:
                            collectFiles[i] = {'name': str(os.path.basename(path)),
                                               'size': str(os.path.getsize(path)),
                                               'path': str(path)}
                            i += 1
                    else:
                        collectFiles[i] = {'name': str(os.path.basename(path)),
                                           'size': str(os.path.getsize(path)),
                                           'path': str(path)}
                        i += 1
    return collectFiles

def RemoveDuplicates(old):
    new = {}
    for old_key, old_value in old.items():
        found = False
        for new_key, new_value in new.items():
            if old_value['name'] == new_value['name'] and old_value['size'] == new_value['size']:
                found = True
        if not found:
            new[old_key] = old_value
    return new

def WriteCollectionToDisk(collection, name):
    folderPath = os.path.dirname(os.path.realpath(__file__))
    fn = os.path.join(folderPath, name)
    file = open(fn,'w+', encoding='cp1252')
    lines = []
    for key, value in collection.items():
        p = value['path'].replace('/','\\')
        n = value['name']
        s = value['size']
        line = n + "||" + s + "||" + p
        lines.append(line.encode("latin-1","ignore"))
    if len(lines) != 0:
        content = b"\n".join(lines)
        content = content.decode('cp1252')
        file.write(content)
    else:
        print("No files found for "+name)
    file.close()
    pass

# Running the program
print("Collecting files...")
d = CollectFiles(path) # First collect all files of the first folder path

print("Removing duplicates...")
d = RemoveDuplicates(d)
print("Writing to file...")
WriteCollectionToDisk(d, saveName) # Write missing file paths to text-file
print("Complete!")