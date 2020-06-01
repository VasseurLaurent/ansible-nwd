import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ansible-nwd',
    packages=setuptools.find_packages(),
    version='0.9',
    license='MIT',
    package_data={'': ['ansible_nwd/templates/markdown.j2']},
    include_package_data=True,
    description='Ansible role automatic documentation',
    author='VASSEUR Laurent',
    author_email='mail.laurentvasseur@gmail.com',
    url='https://github.com/VasseurLaurent/ansible-nwd',
    download_url='https://github.com/VasseurLaurent/ansible-nwd/archive/v0.9.tar.gz',
    keywords=['ansible', 'documentation', 'automation'],
    install_requires=[
        'ruamel.yaml',
        'ruamel.yaml.clib',
        'jinja2-time',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'ansible-nwd=ansible_nwd.main:main',
        ]
    },
    python_requires='>=3.6',
)
