Python3
===========

Description
-----------

This role installs Python3 and set it by default

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

Variable | Type | Mandatory |  Example | Description
--- | --- | --- | --- | --- |
`variable`  | type | false | example | variable description |
`variable2`  | type2 | true | example2 | description2 |


Default Variables
------------------

Variable | Value | Description | Type
--- | --- | --- | --- |
``default_variable1`` | 1.8 | default variable1 version | number |
``default_variable2`` | 2.7 | default variable2 version | number |
``other_variable`` | 3.4 | other variable version | number |
``test`` | 4.5 | n/a | n/a |

Molecule scenario
------------------

### Ec2
Scenario | Platform name | Image name | Instance type |
--- | --- | --- | --- | 
``default`` | debian10 | debian-10-amd64-* | t3.medium



### Docker

Scenario | Platform name | Image |
--- | --- | --- | 
``docker`` | debian10 | geerlingguy/docker-debian10-ansible | 
``docker`` | debian9 | geerlingguy/docker-debian9-ansible |

### Vagrant

Scenario | Platform name | Box |
--- | --- | --- | 
``vagrant`` | debian10 | debian/buster64 |`



Author
-------

Laurent VASSEUR