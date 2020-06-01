from distutils.core import setup
setup(
    name='ansible-nwd',
    packages=['ansible-nwd'],
    version='0.1',
    license='MIT',
    description='Ansible role automatic documentation',
    author='VASSEUR Laurent',
    author_email='mail.laurentvasseur@gmail.com',
    url='https://github.com/VasseurLaurent/ansible-nwd',
    download_url='https://github.com/VasseurLaurent/ansible-nwd/archive/v0.1.tar.gz',
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
    python_requires='>=3.6',
)