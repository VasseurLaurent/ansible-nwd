import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ansible-nwd',
    packages=setuptools.find_packages(),
    version='0.6',
    license='MIT',
    description='Ansible role automatic documentation',
    author='VASSEUR Laurent',
    author_email='mail.laurentvasseur@gmail.com',
    url='https://github.com/VasseurLaurent/ansible-nwd',
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url='https://github.com/VasseurLaurent/ansible-nwd/archive/v0.6.tar.gz',
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
