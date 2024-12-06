from pdf2docx import Converter
import os
from pathlib import Path
import sys

# # # dir_path for input reading and output files & a for loop # # #

inputPath = 'C:/Users/eerde/Desktop/PythonProjects/PythonTest/pdftodocx/input/'
outputPath = 'C:/Users/eerde/Desktop/PythonProjects/PythonTest/pdftodocx/output/'

if len(sys.argv) >= 2 : inputPath = sys.argv[1]
if len(sys.argv) >= 3 : outputPath = sys.argv[2]

print(sys.argv)
def runScript(inputPath, outputPath):
    for file in os.listdir(inputPath):
        cv = Converter(inputPath+file)
        cv.convert(outputPath+Path(file).stem+'.docx', start=0, end=None)
        cv.close()
        print(file)

if __name__ == "__main__" :
    runScript(inputPath,outputPath)