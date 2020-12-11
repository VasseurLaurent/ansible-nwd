Python3
===========

Description
-----------

This role installs Python3 and set it by default

Dependencies
-----------

Name | Source | Version |
--- | --- | --- |
```role1``` | git@gitlab.example.test:user/role1.git | v1.0 |
```role2``` | git@gitlab.example.test:user/role2.git | v1.2 |

Requirements
-------------

### Ansible version

Minimum Ansible version : 2.9

### Platforms

This role will work on the following platforms :

Distribution | Version |
--- | --- |
Debian | buster |
Debian | stretch |

Tasks tags
--------------

These tasks tags are available :

* ``python3``

* ``python3_boto``

* ``python3_packages``

Role Variables
--------------

Variable | Type | Mandatory |  Example | File | Description
--- | --- | --- | --- | --- | --- |
`variable`  | type | false | example | main.yml |  variable description |
`variable2`  | type2 | true | example2 | main.yml |  description2 |
`other`  | other | false | other | other.yml |  other description |
`variablemain`  | type | false | example | main/main.yml |  variable description |


Default Variables
------------------

Variable | Value | Description | Type | File
--- | --- | --- | --- | --- |
``default_variable1`` | 1.8 | default variable1 version | number | main.yml
``default_variable2`` | 2.7 | default variable2 version | number | main.yml
``other_variable`` | 3.4 | other variable version | number | other.yml
``default_main_variable1`` | 1.8 | default variable1 version | number | main/main.yml
``default_main_variable2`` | 2.7 | default variable2 version | number | main/main.yml
``test`` | 4.5 | n/a | n/a | 

Molecule scenario
------------------

### Ec2
Scenario | Platform name | Image name | Instance type |
--- | --- | --- | --- | 
``default`` | debian10 | debian-10-amd64-* | t3.medium




### Vagrant

Scenario | Platform name | Box |
--- | --- | --- | 
``vagrant`` | debian10 | debian/buster64 |`


### Docker

Scenario | Platform name | Image |
--- | --- | --- | 
``docker`` | debian10 | geerlingguy/docker-debian10-ansible | 
``docker`` | debian9 | geerlingguy/docker-debian9-ansible |

### Delegated

| Name | Image_name | Image_owner | Instance_type | Vpc_subnet_id 
| ---| ---| ---| ---| ---
|```debian10```|debian-10-amd64-*|136693071363|t3.medium|xxxxxxxxxxx
|```debian11```|debian-10-amd64-*|136693071363|t3.medium|xxxxxxxxxxx





Author
-------

Laurent VASSEUR