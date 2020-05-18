from os.path import isfile, join
from os import listdir
import re

def parsing_default(path):
    
    path = path + "defaults/"
    list_files_default = [f for f in listdir(path) if isfile(join(path, f))]

    # Add full path to all list files
    list_files_default = [path + s for s in list_files_default]

    for file_default in list_files_default:
        file_opened = open(file_default,'r')
        lines = file_opened.readlines()

        # Regex : # @var variable:description:example

        list_tag = []
        for line in lines:
            regex_tag = re.findall(
                '^\s*# @var ([\.0-9a-zA-Z_-]*):([\.0-9a-zA-Z_-]*):([\.0-9a-zA-Z_-]*)', line)

            if len(regex_tag) != 0:
                list_tag.append(regex_tag)

        print(list_tag[0][0][0])
        file_opened.close()
