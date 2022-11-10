import os
import json
import sys
import shutil

EXTENSION = ".txt"

def get_all_txt_file(source_path): # get all file path in directory "data" with extension .txt
    txt_path = []
    
    for root, dirs, file in os.walk(source_path):
        for f in file:
            if EXTENSION in f:
                path = os.path.join(source_path, f)
                txt_path.append(path)
        break
    
    return txt_path

def create_dir(target_path): # create directory with "target name"
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    else:
        print("There is already file with that name!")
        
def copy_to(source_path, target_path): # copy all files with extension .txt to directory "target"
    shutil.copy(source_path, target_path)
    
def new_names(target_path): # Remove extension in file name
    new_name_list = []
    
    for path in target_path:
        _, name = os.path.split(path)
        finall_name = name.replace(EXTENSION, "")
        new_name_list.append(finall_name)
    return new_name_list
    
def create_metadata(target_path, copied_file): # create metadata of copied files
    data = {
        "File name": copied_file,
        "Number of copied file": len(copied_file)
    }
    
    with open(target_path, 'w') as f:
        json.dump(data, f)

def main(source, target):
    cwd = os.getcwd() # get current working directory
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    
    txt_path_file = get_all_txt_file(source_path)
    create_dir(target_path)
    
    for f in txt_path_file:
        copy_to(f, target_path)
        
    names = new_names(txt_path_file)
    json_metadata = os.path.join(target_path, "metadata.json")
    create_metadata(json_metadata, names)

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 3:
        raise Exception("You must enter source and target name directory - only")
    source, target = argv[1:]
    main(source, target)