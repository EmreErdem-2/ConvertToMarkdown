import os
import sys
from pathlib import Path
import shutil


#Creates a one media folder for a section
#Renames all the media files according to their name + media

inputPath = 'C:/Users/eerde/Desktop/PythonProjects/PythonTest/pdftodocx/input/'
inputPath2 = "C:/Users/eerde/Desktop/PythonProjects/PythonTest/pdftodocx/output/"
outputPath = "C:/Users/eerde/Desktop/PythonProjects/PythonTest/pdftodocx/output/MarkdownFiles/"

if len(sys.argv) >= 2 : inputPath = sys.argv[1]
if len(sys.argv) >= 3 : outputPath = sys.argv[2]

def removeDirectories(folderPath):
    print(os.listdir(folderPath))
    for dir in os.listdir(folderPath):
        fullPathDir = folderPath+dir
        if dir == "_attachments" or Path(dir).suffix != '':
            continue #dont delete _attachments
        try: 
            shutil.rmtree(fullPathDir) 
            print("Removed: "+fullPathDir)
        except OSError as e:
            print(f"Error: {fullPathDir} : {e.strerror}")

def renameAndMove(folderPath,attachmentPath):
    for subdir, dirs, files in os.walk(folderPath):
        for file in files:
            if Path(file).suffix == ".md" or subdir == attachmentPath:
                continue #skip markdown files
            oldImageNamePath = subdir+"\\"+file
            newImageName = subdir.split(folderPath)[1].split("\\")[0].split("Media")[0][1:] + file.title()
            newImageNamePath = attachmentPath + "/" + newImageName
            print("OLD IMAGE PATH: "+oldImageNamePath)
            os.rename(oldImageNamePath, newImageNamePath)
            print("Image renamed and moved: " + newImageName)
        print("attachments check")
    print("***Rename and Move Media Files is Done***")

def createAttachmentFolder(attachmentPath):
    if not os.path.isdir(attachmentPath):
        print("No attachment folder found. Creating attachment folder..." + attachmentPath)
        os.mkdir(attachmentPath)


def rearrangeMediaFiles(outputPath):
    attachmentPath = outputPath + "_attachments"

    createAttachmentFolder(attachmentPath)
    renameAndMove(outputPath,attachmentPath)        
    removeDirectories(outputPath)


if __name__ == "__main__":
    rearrangeMediaFiles(outputPath)
        
