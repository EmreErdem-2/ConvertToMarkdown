import re
import os
import sys

def find_md_files(path):
    file_list = os.listdir(path)
    return [file for file in file_list if file.endswith('.md')]

def find_file_paths(file_path,location_file):
    print("inside find_file_paths")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regular expression to match file paths
        pattern = re.escape(location_file) + r'[\w\/\.-]*'
        print("pattern : ", pattern)
        file_paths = re.findall(pattern, content)      
        print("file_paths : ", file_paths)
        return file_paths
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def renameFilePath(file_name, file_path_markdown, isRenamedToFullPath=False):
    print("In renameFile")
    print("file_name : ",file_name)
    print("file_path_markdown : ",file_path_markdown)
    image_name = os.path.basename(file_path_markdown).title()
    print("Image_Name : ", image_name)
    file_path_reducted = file_path_markdown.split(file_name)
    print("file_path_reducted : ", file_path_reducted)
    if isRenamedToFullPath:
        renamedPath = file_path_reducted[0][:-1]+"_attachments/"+file_name+image_name
    else:
        renamedPath = file_name+image_name
    return renamedPath

def replace_file_paths(file_path):
    try:
        print("inside open")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            base_name = os.path.basename(file.name)
            name_without_suffix = os.path.splitext(base_name)[0]
        
        location_file = file_path.split(name_without_suffix)[0]
        
        print(base_name)
        print(name_without_suffix)
        print(location_file)
        pathsInFile = find_file_paths(file_path,location_file)
        for pathInFile in pathsInFile:
            print("PathInFile : ",pathInFile)
            renamedPath = renameFilePath(name_without_suffix,pathInFile)
            print("RenamedPath : ",renamedPath)
            # Use re.sub to replace all occurrences of the old path with the new path
            content = re.sub(re.escape(pathInFile), renamedPath, content)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        return "File paths replaced successfully."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def runRearrangeMediaLinks(location_file):
    md_files = find_md_files(location_file)
    
    for file in md_files:
        print("------------------------------",file,"------------------------------")
        file_path = location_file + file
        # print(file_path)
        print(replace_file_paths(file_path))


location_file = r"C:/Users/eerde/Desktop/PythonProjects/PythonTest/pdftodocx/output/MarkdownFiles/"

if len(sys.argv) >= 2 : location_file = sys.argv[1]

if __name__ == "__main__":
    runRearrangeMediaLinks(location_file)
