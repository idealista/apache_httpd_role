![Logo](https://raw.githubusercontent.com/idealista/apache_httpd-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/apache_httpd-role.png)](https://travis-ci.org/idealista/apache_httpd-role)

# Apache HTTP Server Ansible role

This Ansible role installs an Apache HTTP server in a Debian environment. The server is installed using the sources and loading just the predefined modules.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your Ansible playbook. Once launched, it will install a [Apache HTTP Server](https://httpd.apache.org/) in a Debian system.

### Prerequisities

Ansible 2.4.0.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) (version 1.25) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) or [Docker](https://www.docker.com/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

``` yml
- src: idealista.apache_httpd-role
  version: 1.0.0
  name: apache_httpd
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

``` yml
---
- hosts: someserver
  roles:
    - role: apache_httpd
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

Bear in mind that the role deploys the default Apache httdp config file. If you want to use yours (something that we strongly recommend), place it under the directory referred by the variable `apache_extra_conf_template_path`. If you need any inspiration, a good template to start with could be the one in `tests/templates/apache/conf/httpd.conf.j2`.

## Testing

### Using Vagrant as provider
```
molecule test
```

### Using Docker as provider
```
molecule test --driver docker
```

See molecule.yml to check possible testing platforms. As a reminder, our tests are just compatible with Molecule 1.x

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/apache_httpd-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/apache_httpd-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
