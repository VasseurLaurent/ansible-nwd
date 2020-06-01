import argparse
from .parsing import parsing
import os

from jinja2 import Environment, FileSystemLoader


def main():

    role = False
    molecule = False
    role_model = ['meta', 'templates', 'handlers',
                  'tasks', 'defaults', 'files', 'vars', 'tests']

    parser = argparse.ArgumentParser(
        description='Ansible never write the doc help')

    parser.add_argument('-m', '--module',  type=str,
                        help='Module directory path', required=False, default='.')
    parser.add_argument('-r', '--readme', type=str,
                        help='Define readme file name', required=False, default='README.md')
    parser.add_argument('-t', '--template', type=str,
                        help='Define template file ', required=False, default='markdown.j2')

    arguments = parser.parse_args()

    # Format arguments + variable

    if arguments.module[-1] != "/":
        arguments.module = arguments.module + "/"

    role_name = os.path.basename(os.path.realpath(arguments.module))
    role_full_path = os.path.realpath(arguments.module)
    script_folder = os.path.dirname(os.path.realpath(__file__))

    # print("role_name: " + role_name)
    # print("role_full_path: " + role_full_path)

    # Check if the directory is a module directory

    dir_list = [directory for directory in os.listdir(
        arguments.module) if os.path.isdir(arguments.module+directory)]

    if all(item in dir_list for item in role_model) is True:
        role = True

    else:
        print("Your role doesn't follow Ansible galaxy file tree, please use ansible-galaxy init to create your role")

    # Check if it exists a molecule directory

    if 'molecule' in dir_list:
        molecule = True

    # Create README.MD file

    if role is True:
        # Gathers information from parsing
        list_molecule = {}
        list_tag_default = parsing.parsing_default_tag(path=role_full_path)
        list_default_variable = parsing.parsing_default_variable(
            path=role_full_path)
        meta = parsing.parsing_meta(path=role_full_path)
        list_tasks = parsing.parsing_tasks(path=role_full_path)

        if molecule is True:
            list_molecule = parsing.parsing_molecule(path=role_full_path)

        # Load template
        env = Environment(loader=FileSystemLoader(
            script_folder))
        template = env.get_template(arguments.template)

        readme = template.render(name=role_name, default_tag=list_tag_default,
                                 default_value=list_default_variable, meta=meta, molecule=list_molecule, tasks=list_tasks)
        f = open(role_full_path + "/" + arguments.readme, "w+")
        f.write(readme)
        f.close()


if __name__ == "__main__":
    main()
