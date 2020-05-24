from os.path import isfile, join
from os import listdir
import yaml
import re

def parsing_default_tag(path):
    
    path = path + "/defaults/"

    list_files_default = [f for f in listdir(path) if isfile(join(path, f))]

    # Add full path to all list files
    list_files_default = [path + s for s in list_files_default]

    for file_default in list_files_default:
        file_opened = open(file_default,'r')
        lines = file_opened.readlines()

        # Regex : # @var variable:description:type:example:mandatory

        list_tag = []
        for line in lines:

            pattern = re.compile(
                '^\s*# @var (?P<name>[\.0-9a-zA-Z_-]*):(?P<description>[\.0-9a-zA-Z_-]*):(?P<type>[\.0-9a-zA-Z_-]*):(?P<example>[\.0-9a-zA-Z_-]*):(?P<mandatory>[\.0-9a-zA-Z_-]*)')

            for m in pattern.finditer(line):
                list_tag.append(m.groupdict())

        file_opened.close()
        return list_tag

def parsing_default_variable(path):

    default_variable = []
    path = path + "/defaults/"

    list_files_default = [f for f in listdir(path) if isfile(join(path, f))]

    # Add full path to all list files
    list_files_default = [path + s for s in list_files_default]

    for file_default in list_files_default:
        with open(file_default) as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
            # print(doc)
            for key, value in doc.items():
                temp = { key : value }
                default_variable.append(temp)
    
    print(default_variable[0])
    return default_variable
            



def parsing_meta(path):
    meta = {}
    path = path + "/meta/main.yml"
    with open(path, 'r') as f:
        doc = yaml.safe_load(f)
        meta = {'author': doc["galaxy_info"]["author"],
                'description': doc["galaxy_info"]["description"],
                'min_ansible_version': doc["galaxy_info"]["min_ansible_version"],
                'platforms': doc["galaxy_info"]["platforms"]}
                
        return meta


