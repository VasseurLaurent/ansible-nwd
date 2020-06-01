# Ansible Never Write the Doc

[![Build Status](https://travis-ci.com/VasseurLaurent/ansible-nwd.svg?branch=master)](https://travis-ci.com/VasseurLaurent/ansible-nwd) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI version](https://badge.fury.io/py/ansible-nwd.svg)](https://badge.fury.io/py/ansible-nwd) ![Upload Python Package](https://github.com/VasseurLaurent/ansible-nwd/workflows/Upload%20Python%20Package/badge.svg)

## Introduction

``Ansible Never Write the Doc`` provides you an automatic way to create Ansible roles documentation.

It parses all Ansible roles folders and gathers information to write them into a ``Readme.md`` for you.

``Ansible-nwd`` is also compatible with ``molecule`` , it will parse your different scenarios and write them into your documentation file.

## Get started with pip !

`Ansible-nwd` is really easy to use.

First of install it with pip :

```shell
pip install ansible-nwd
```

Now you can use it on your ansible role !

FIll in your ansible role to follown ```Ansible-nwd``` pattern and :

```shell
ansible-nwd -m 'path/to/your/role'
```

or

```shell
cd 'path/to/your/role' && ansible-nwd
```

That's it ! Your documentation is ready

## Get started with docker !

You can simply run the docker in your Ansible role folder such as :

```shell
docker run -v $(pwd):/data laurentvasseur/ansible-nwd
```

That's it ! Your documentation is ready

## How does it work ?

``Ansible-nwd`` will parse your Ansible roles folders and , according to the folder and some patterns found in your yaml files it will gather information for you.

Currently, it parses these following folders:

* default

* meta

* molecule

* tasks

Check below to know which pattern are recognized.

### Default

In the folder ``default`` you can have two different patterns:

* Default variables defined
* Variables not defined by default but useful for your role

#### Default variables defined

If you define a default variable, they will be retrieved by ``Ansible-nwd`` and their default values will be written in the documentation file.

Moreover, you can add information about these variables following this pattern:

```yaml
your_variable: your_value # description of your variable:type
```

For example :

```yaml
default_variable1: 1.8 # default variable1 version:number
default_variable2: 2.7 # default variable2 version:number
other_variable: 3.4 # other variable version:number
test: 4.5
```

Will create this entry in your documentation file :


Variable | Value | Description | Type
--- | --- | --- | --- |
``default_variable1`` | 1.8 | default variable1 version | number |
``default_variable2`` | 2.7 | default variable2 version | number |
``other_variable`` | 3.4 | other variable version | number |
``test`` | 4.5 | n/a | n/a |

### Variables not defined by default

There are some variables that you cannot define by default or not mandatory for your role.

With  ```Ansible-nwd ``` you can define some variables thank to tags in comment.

For example, if you want to specify a variable which is not defined as default you can do it following this pattern:

```yaml
# @var variable:description:type:example:mandatory(bool)
```

For example :

```yaml
# @var variable:variable description:type:example:false
# @var variable2:description2:type2:example2:true
```

Will create this entry in your documentation file :

Variable | Type | Mandatory |  Example | Description
--- | --- | --- | --- | --- |
`variable`  | type | false | example | variable description |
`variable2`  | type2 | true | example2 | description2 |

### Meta

In the meta folder, ``Ansible-nwd`` will gather these following information:

* Author
* Description
* Minimum Ansible Version
* Platforms

### Molecule

In the folder molecule, ``Ansible-nwd`` will parse each subfolders (we consider one driver per folder ) and will gather information about available test plaforms written in the file ```molecule.yml``` .

For now only 3 drivers are gathered by ```Ansible-nwd``` :

* docker
* vagrant : https://pypi.org/project/molecule-vagrant/
* ec2 : https://pypi.org/project/molecule-ec2/

For example :

```yaml
driver:
  name: docker

platforms:
  - name: debian10
    image: geerlingguy/docker-debian10-ansible
    pre_build_image: true
  - name: debian9
    image: geerlingguy/docker-debian9-ansible
    pre_build_image: true
```

Will create the following entry in the documentation :

Scenario | Platform name | Image |
--- | --- | --- | 
``docker`` | debian10 | geerlingguy/docker-debian10-ansible | 
``docker`` | debian9 | geerlingguy/docker-debian9-ansible |

### Tasks

A common workflow when developing an Ansible roles is to add only ```include``` command in the file ```tasks/main.yml```. It can be really useful to add tags to these include to allow shorter deployment.

```Ansible-nwd``` will read these tags and write them in the documentation.

For example: 

```yaml
# tasks file for python3

  - include: packages.yml
    tags:
      - python3_packages
      - python3
  
  - include: boto.yml
    tags:
      - python3_boto
      - python3
```

Will create the following entry in the documentation:

These tasks tags are available :

* ``python3``

* ``python3_boto``

* ``python3_packages``
