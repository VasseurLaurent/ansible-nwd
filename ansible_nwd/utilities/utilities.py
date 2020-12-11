import glob
import os

def get_list_files(path,list_files):
    for filename in glob.iglob(path + '**/*', recursive=True):
        if os.path.isfile(filename):
            relative_paths = os.path.relpath(filename, path)
            list_files.append(relative_paths)

    return list_files
