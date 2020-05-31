# Ansible Never Write the Doc

[![Build Status](https://travis-ci.com/VasseurLaurent/ansible-nwd.svg?branch=master)](https://travis-ci.com/VasseurLaurent/ansible-nwd)

## Introduction

``Ansible Never Write the Doc`` provides you an automatic way to create Ansible roles.

It parses all Ansible roles folder and get gathers information to write them in a ``Readme.md`` for you.

``Ansible-nwd`` is also compatible with ``molecule`` , it will parse your different scenario and write them into your documentation file.

## How does it work ?

``Ansible-nwd`` will parse your folders Ansible roles and according to the folder and some patterns found in your yaml files it will gathers information for you.

Currently, it parses these following folders:

* default

* meta

* molecule

* tasks

Check below to know which pattern are recognized.

### Default

In the folder ``default`` you can have two different pattern:

* Default variables defined
* Variables not defined by default but useful for your role

#### Default variables defined

If you define default variable, they will be retrieve by ``Ansible-nwd`` and their default value will be written in the documentation file.

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

For example, if you want to specify a variable which is not defined as default you can do it following the following pattern:

```yaml
# @var variable:description:type:example:mandatory(bool)
```

For example :

```yaml
# @var variable:variable description:type:example:false
# @var variable2:description2:type2:example2:true
```

WIll create this entry in your documentation file :

Variable | Type | Mandatory |  Example | Description
--- | --- | --- | --- | --- |
`variable`  | type | false | example | variable description |
`variable2`  | type2 | true | example2 | description2 |