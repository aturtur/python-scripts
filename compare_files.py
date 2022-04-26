# Compares two folder paths and prints missing files
# 22.04.2022 Arttu Rautio
# Python 3 or newer

# Libraries
import os
import sys
import re

# ------------- Folder paths -------------
# Folder path that should have more files (HDD)
pathA = ""

# Folder path that should have less files (Server)
pathB = ""
bufferPath = ""
useBuffer = False

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

def Compare(dirA, dirB):
    missingFiles = dirA
    try:
        for key, itemA in list(dirA.items()):
            for j, itemB in dirB.items():
                if itemA['name'] == itemB['name']:
                    if itemA['size'] == itemB['size']:
                        missingFiles.pop(key)
    except KeyError:
        print("Error!")

    return missingFiles

def WriteMissingFilesToFile(collection):
    folderPath = os.path.dirname(os.path.realpath(__file__))
    fn = os.path.join(folderPath, "missing_files.txt")
    file = open(fn,'w+', encoding='cp1252')
    lines = []

    for key, value in collection.items():
        p = value['path'].replace('/','\\').encode("latin-1","ignore")
        print("Missing file found: " + p.decode('cp1252'))
        lines.append(p)
    if len(lines) != 0:
        content = b"\n".join(lines)
        content = content.decode('cp1252')
        file.write(content)
    else:
        print("No missing files found!")
    file.close()

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

def CreateDictFromFile(dictPath):
    d = {}
    fn = open(dictPath)
    for i, line in enumerate(fn):        
        n, s, p = line.split('||')
        d[i] = {'name': n,
                'size': s,
                'path': p}

    return d

# Running the program
pathACheck = os.path.isdir(pathA)
pathBCheck = os.path.isdir(pathB)
error = False
#if pathACheck:

print("Collecting files from pathA...")
dirA = CollectFiles(pathA) # First collect all files of the first folder path
#else:
#    print("Directory not found: " + str(pathA))
#    error = True

if pathBCheck:
    print("Collecting files from pathB...")
    dirB = CollectFiles(pathB) # Then collect all files of the second folder path
else:
    print("Directory not found: " + str(pathB))
    error = True

if not error:
    print("Removing duplicates from A...")
    dirA = RemoveDuplicates(dirA)

    if not useBuffer:
        print("Removing duplicates from B...")
        dirB = RemoveDuplicates(dirB)
    else:
        print("Reading buffer file...")
        dirB = CreateDictFromFile(bufferPath)

    print("Comparing files...")
    missingFiles = Compare(dirA, dirB) # Compare folders and return dictionary of missing files

    print("Writing missing files to file...")
    WriteMissingFilesToFile(missingFiles) # Write missing file paths to text-file
    print("Complete!")

else:
    print("Error!")