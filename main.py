import argparse
import os
from parsing import parsing_default_tag, parsing_meta
from jinja2 import Environment, FileSystemLoader

role = False
molecule = False
role_model = ['meta','templates','handlers','tasks','defaults','files','vars','tests']

parser = argparse.ArgumentParser(description='Ansible never write the doc help')

parser.add_argument('-m', '--module' ,  type=str, help='Module directory path', required=False, default='.')
parser.add_argument('-r', '--readme', type=str, help='Define readme file name', required=False, default='README.MD')
parser.add_argument('-t', '--template', type=str, help='Define template file ', required=False, default='markdown.j2')

arguments = parser.parse_args()


# Format arguments + variable

if arguments.module[-1] != "/":
    arguments.module = arguments.module + "/"

role_name = os.path.basename(os.path.realpath(arguments.module))
role_full_path = os.path.realpath(arguments.module)
script_folder = os.path.dirname(os.path.realpath(__file__))

print("role_name: " + role_name)
print("role_full_path: " + role_full_path)

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

# Create README.MD file

if role is True:
    # Gathers information from parsing
    list_tag_default = parsing_default_tag(path=role_full_path)
    meta = parsing_meta(path=role_full_path)

    # Load template
    env = Environment(loader=FileSystemLoader(script_folder + '/templates'))
    template = env.get_template(arguments.template)

    readme = template.render(name=role_name,default=list_tag_default,meta=meta)
    f = open(role_full_path + "/" + arguments.readme, "w+")
    f.write(readme)
    f.close()
