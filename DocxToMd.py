import subprocess
import sys
#pandoc --extract-media $("./"+$MediaFolderName) $($DocxFileName+".docx") -o

# fileout = os.path.splitext(filename)[0] + ".md"
# args = ['pandoc', filename, '-o', fileout]
# subprocess.Popen(args)


def runPowerShell(cmd,args):
    argList = ["powershell"] + ["-ExecutionPolicy"] + ["Bypass"] + ["-File"] + [cmd] + args
    completed = subprocess.run(argList, shell=True)

    return completed

inputPath = './'
outputPath = "./"

if len(sys.argv) >= 2 : inputPath = sys.argv[1]
if len(sys.argv) >= 3 : outputPath = sys.argv[2]

print(sys.argv)

def runScript(inputPath,outputPath):

    scriptArgs = [inputPath, outputPath]
    scriptReturn = runPowerShell("./DocxToMd.ps1", scriptArgs)

    print(scriptReturn)

if __name__ == "__main__" :
    runScript(inputPath,outputPath)