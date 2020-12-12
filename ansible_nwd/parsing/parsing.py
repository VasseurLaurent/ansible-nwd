from os.path import isfile, join, exists
from os import listdir
from collections import defaultdict
import ruamel.yaml
import re
import sys
import glob
from ansible_nwd.utilities.utilities import *
from collections import OrderedDict

def parsing_default_tag(path):

    path = path + "/defaults/"
    list_files_relpath_default = []
    list_tag = []

    get_list_files(path, list_files_relpath_default)


    # Parse all files in defaults to get tags

    for relpath in list_files_relpath_default:

        file_opened = open(os.path.join(path,relpath),'r')
        lines = file_opened.readlines()

        # Regex : # @var variable;description;type;example;mandatory

        for line in lines:
            pattern = re.compile(
                '^\s*# @var (?P<name>[^;\n]*);(?P<description>[^;\n]*);(?P<type>[^;\n]*);(?P<example>[^;\n]*);(?P<mandatory>[^;\n]*)')
            for m in pattern.finditer(line):
                output_regex = m.groupdict()
                output_regex['file'] = relpath
                list_tag.append(output_regex)
            file_opened.close()
    return list_tag

def parsing_default_variable(path):

    default_variable = {}
    default_variable_defined_without_comment = {}
    path = path + "/defaults/"
    list_files_default = []

    get_list_files(path,list_files_default)
    # Add full path to all list files

    for file_default in list_files_default:
        with open(os.path.join(path,file_default)) as f:
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
                    '^#\s*(?P<description>[^;\n]*);(?P<type>[^;\n]*)')

                for m in pattern.finditer(comment):
                    output_regex = m.groupdict()
                    output_regex['file'] = file_default
                    default_variable[key] = output_regex

            # Get value for default value

            for key, value in file_loaded.items():
                default_variable_defined_without_comment[key] = value

    # Merge dictionnaries with and without comment

    for item in default_variable_defined_without_comment:
        if item in default_variable:
            default_variable[item].update(
                value=str(default_variable_defined_without_comment[item]))
        else:
            default_variable[item] = {
                'value': str(default_variable_defined_without_comment[item])}
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

def parsing_dependencies(path):
    dependencies = {}
    path = path + "/meta/requirements.yml"
    if isfile (path):
        with open(path) as f:
            yaml = ruamel.yaml.YAML()
            file_loaded = yaml.load(f)
            if file_loaded:
                for item in file_loaded:
                    dependencies[item['name']] = {
                        'src': item['src'], 'version': item['version']}
    return dependencies


def parsing_molecule(path):
    path = path + "/molecule/"
    molecule = {}

    list_scenario = [f for f in listdir(path)]
    for scenario in list_scenario:
        molecule_scenario = path + scenario + '/molecule.yml'
        if not exists(molecule_scenario):
            continue
        with open(molecule_scenario, 'r') as f:
            yaml = ruamel.yaml.YAML()
            doc = yaml.load(f)            
            molecule[scenario] = {'driver': doc['driver']['name'] , 'platforms': doc['platforms']}

            # If molecule driver is delegated we retreive all keys to be able to write the documentation
            if molecule[scenario]['driver'] == "delegated" :
                
                for platform in molecule[scenario]['platforms'] :
                    keys = dict(platform)
                    molecule[scenario]['keys'] = {'keys': keys.keys()}
    return molecule

def parsing_tasks(path):
    tags = []
    path = path + "/tasks/main.yml"
    with open(path, 'r') as f:
        yaml = ruamel.yaml.YAML()
        file_loaded = yaml.load(f)
        for item in file_loaded:
            if 'tags' not in item:
                continue
            for tag in item['tags']:
                if tag not in tags:
                    tags.append(tag)
    return sorted(tags)

