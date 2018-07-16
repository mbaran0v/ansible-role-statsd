# Ansible role: Statsd

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-statsd.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-statsd)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![GitHub tag](https://img.shields.io/github/tag/mbaran0v/ansible-role-statsd)](https://github.com/mbaran0v/ansible-role-statsd/tags)

Ansible role for [Statsd](https://github.com/etsy/statsd). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* Ubuntu 14.04
* Debian 9
* Debian 8
* CentOS 7
* CentOS 6

Requirements
------------

You should install Node.js on server for this role (i use [geerlingguy/ansible-role-nodejs](https://github.com/geerlingguy/ansible-role-nodejs.git) for this).

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
statsd_version: v0.8.0
statsd_title: statsd
statsd_root_dir: /opt/statsd
statsd_nodejs: /usr/bin/nodejs
statsd_user: _statsd
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: statsd
  vars:
    nodejs_version: "6.x"
    nodejs_install_npm_user: root
  roles:
      - role: geerlingguy.nodejs
      - role: mbaran0v.statsd
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by Maxim Baranov.
