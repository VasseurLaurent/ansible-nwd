import argparse
import os
from parsing import parsing_default_tag, parsing_meta
from jinja2 import Environment, FileSystemLoader

role = False
molecule = False
role_model = ['meta','templates','handlers','tasks','defaults','files','vars','tests']

parser = argparse.ArgumentParser(description='Ansible never write the doc help')

parser.add_argument('-m', '--module' ,  type=str, help='Module directory path', required=False,default='.')
parser.add_argument('-r', '--readme', type=str, help='Define readme file name', required=False, default='README.MD')
parser.add_argument('-t', '--template', type=str, help='Define template file ', required=False, default='markdown.j2')

arguments = parser.parse_args()


# Format arguments

if arguments.module[-1] != "/":
    arguments.module = arguments.module + "/"


# Check if the directory is a module directory 

dir_list = [directory for directory in os.listdir(
    arguments.module) if os.path.isdir(arguments.module+directory)]

if all(item in dir_list for item in role_model) is True:
    role = True
    print("Role confirmed")

else:
    print("Your role doesn't follow Ansible galaxy file tree, please use ansible-galaxy init to create your role")

# Check if it exists a molecule directory

if 'molecule' in dir_list :
    molecule = True
    print("Molecule detected")

print(arguments.module)

# Create README.MD file

if role is True:
    # Gathers information from parsing
    name = os.path.basename(arguments.module[:-1])
    list_tag_default = parsing_default_tag(path=arguments.module)
    meta = parsing_meta(path=arguments.module)

    # Load template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(arguments.template)

    readme = template.render(name=name,default=list_tag_default,meta=meta)
    f = open(arguments.module + arguments.readme, "w+")
    f.write(readme)
    f.close()
