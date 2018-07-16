# Ansible role: Statsd

Ansible role for [Statsd](https://github.com/etsy/statsd). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* Ubuntu 14.04
* Debian 9
* Debian 8
* CentOS 7
* CentOS 6

Requirements
------------

None.

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
  roles:
      - { role: mbaran0v.statsd }
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by Maxim Baranov.
