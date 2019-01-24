#---------------------------------------- 
# @author : Amjad Yousef Majid
# @date   : Jan. 24, 2019
#---------------------------------------- 
#
## This script goes through files in a given directory (folder) and replace a
# phrase with a new one. 

import re
import shutil
import glob
import sys
import os

#TODO handle exceptions, 

def main():
    # prompt the user for the directory path
    dir_path = user_input("Enter directory path: ")
    file_pattern = user_input("Enter files names pattern (i.e. *.txt): ")
    # prompt the user for the targeted string 
    old_line = user_input("Enter a string be replaced (can be a regex [i.e. colou?r] ) : ")
    # prompt the user for the new string 
    new_line = user_input("Enter the new string: ")
    
    # create a temporary directory 
    tmp_path = create_tmp_dir(dir_path)
    # loop through all the files in a directory
    files = get_files(dir_path, file_pattern) 
    # access each file individually 
    # check for IO exceptions
    # read the file line by line 
    # replace the targeted string 
    update_files(dir_path, files, old_line, new_line) 
    # move all the files from the temporary directory to the original one
    move_files(dir_path, tmp_path, files) 
    # done

#-------------------------------------------------------------------------------- 
def create_tmp_dir(parent_dir):
    """create_tmp_dir(dir) takes a path to a directory and create a child 
    directory in it called `tmp` 
    @param dir: a path to a directory (folder)"""

    tmp_dir = os.path.join(parent_dir, 'tmp')
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    return tmp_dir
#-------------------------------------------------------------------------------- 
def user_input(prompt=""):
    """ user_input(msg) 
       prompts the user for input. It recognizes the version of Python and uses 
       the correct `input` function from Python
       @param msg: a message to displayed to the user """
    
    if sys.version_info[0] < 3:
        u_input = raw_input(prompt)
    else:
        u_input = input(prompt) 
    return u_input            

#-------------------------------------------------------------------------------- 
def update_files(path, files, old_str, new_str):
    p = re.compile(old_str)
    for f in files:
        with open( os.path.join(path,"tmp/"+f), "w") as ofObj:
            with open(os.path.join(path,f)) as ifObj:
                for l in ifObj:
                    l = p.sub(new_str,l)
                    ofObj.write(l)
    
#-------------------------------------------------------------------------------- 
def move_files(old_path,new_path, files):
    for f in files:
        shutil.copy( os.path.join(new_path,f), old_path)
    shutil.rmtree(new_path)
#-------------------------------------------------------------------------------- 
def get_files(path, file_pattern):
    """get a list of files in a directory"""
    cur_path = os.getcwd()
    os.chdir(path)
    files =  glob.glob(file_pattern)
    os.chdir(cur_path)
    return files

#-------------------------------------------------------------------------------- 
def child_dirs(path):
    """child_dirs(path) takes a path to a directory and return a list of its 
    immediate subdirectories"""
    return[(d.rstrip('/')).lstrip(path+"/") for d in glob.glob(path+"/*/")]    



if __name__ == "__main__": main()



