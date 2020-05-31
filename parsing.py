from os.path import isfile, join
from os import listdir
from collections import defaultdict
import ruamel.yaml
import re
import sys

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
                '^\s*# @var (?P<name>[\.0-9a-zA-Z_-]*):(?P<description>[\.\0-9a-zA-Z_-]*):(?P<type>[\.\S0-9a-zA-Z_-]*):(?P<example>[\.0-9a-zA-Z_-]*):(?P<mandatory>[\.0-9a-zA-Z_-]*)')

            for m in pattern.finditer(line):
                list_tag.append(m.groupdict())

        file_opened.close()
        return list_tag

def parsing_default_variable(path):

    default_variable = {}
    default_variable_defined_without_comment = {}
    path = path + "/defaults/"

    list_files_default = [f for f in listdir(path) if isfile(join(path, f))]

    # Add full path to all list files
    list_files_default = [path + s for s in list_files_default]


    for file_default in list_files_default:
        with open(file_default) as f:
            yaml = ruamel.yaml.YAML()
            file_loaded = yaml.load(f)

            # Get comment for default variable
            root_comment = file_loaded.ca

            for key in root_comment.items:

                # Format the comment

                comment = root_comment.items[key][2].value

                while comment.endswith("\n"):
                    comment = comment[:-1]

                pattern = re.compile(
                    '^#\s*(?P<description>[\.\0-9a-zA-Z_-]*):(?P<type>[\.\S0-9a-zA-Z_-]*)')

                for m in pattern.finditer(comment):
                    default_variable[key] = m.groupdict()

            # print(default_variable)

            # Get value for default value

            for key, value in file_loaded.items():
                default_variable_defined_without_comment[key] = value

    # Merge dictionnaries with and without comment

    for item in default_variable_defined_without_comment:
        if item in default_variable:
            default_variable[item].update(
                value=default_variable_defined_without_comment[item])
        else:
            default_variable[item] = {
                'value': default_variable_defined_without_comment[item]}

    return default_variable
            

def parsing_meta(path):
    meta = {}
    path = path + "/meta/main.yml"
    with open(path, 'r') as f:
        yaml = ruamel.yaml.YAML()
        doc = yaml.load(f)
        meta = {'author': doc["galaxy_info"]["author"],
                'description': doc["galaxy_info"]["description"],
                'min_ansible_version': doc["galaxy_info"]["min_ansible_version"],
                'platforms': doc["galaxy_info"]["platforms"]}
                
        return meta


def parsing_molecule(path):
    path = path + "/molecule/"
    molecule = {}

    list_scenario = [f for f in listdir(path)]

    for scenario in list_scenario:
        with open(path + scenario + '/molecule.yml', 'r') as f:
            yaml = ruamel.yaml.YAML()
            doc = yaml.load(f)

            molecule[scenario] = {'driver': doc['driver']['name'] , 'platforms': doc['platforms']}

    return molecule

def parsing_tasks(path):
    tags = []
    path = path + "/tasks/main.yml"
    print(path)
    with open(path, 'r') as f:
        yaml = ruamel.yaml.YAML()
        file_loaded = yaml.load(f)
        for item in file_loaded:
            for tag in item['tags']:
                if tag not in tags:
                    tags.append(tag)
    return sorted(tags)

